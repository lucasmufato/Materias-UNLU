<?php
include_once "Articulo.php";
include_once "ImageSaver.php";
include_once "Comentario.php";

class Controlador{
    private static $dirArticulos="articulos/";
    private static $bd=true;
    private $bd_name="PAW";
    private $bd_host="localhost";
    private $bd_port=5432;
    private $bd_user="lucas";
    private $bd_pass="lucas";
    private $conn;
    
    function __construct(){
        //constructor vacio
        if(Controlador::$bd){
            $this->conn = new PDO("pgsql:host=$this->bd_host;dbname=$this->bd_name", $this->bd_user, $this->bd_pass) or die("no me pude conectar a la BD");
            $this->conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        }
    }
    
    function getLastID(){
        if(Controlador::$bd){
            return $this->conn->lastInsertId();
        }else{
            //agarro el ultimo archivo, le saco el .dat lo transformor a entero y lo aumento en 1
            $files ='articulos/';
            $nroId=1;
            while(true){
                $f = $files . $nroId . ".dat";
                if(!file_exists($f)){
                    return $nroId;
                }
                $nroId++;
            }
        }
    }
    
    function tomarDatosPost(){
        $articulo = new Articulo();
        $articulo->titulo=$_POST['titulo'];
        $articulo->descripcion=$_POST['descripcion'];
        $articulo->imagen=ImageSaver::guardarImagen();
        $articulo->fecha = date("Y/m/d");
        $articulo->comentarios=null;
        $articulo->activo=true;
        return $articulo;
    }
    
    function nuevo(){
        $articulo = $this->tomarDatosPost();
        if(Controlador::$bd){
            $this->nuevoEnBD($articulo);
        }else{
            $articulo->id= $this->getLastID();
            $this->nuevoEnArchivo($articulo);
        }        
    }
    
    function modificar(){
        $articulo =  $this->tomarDatosPost();
        $articulo->id= $_POST['id'];
        if(Controlador::$bd){
            $this->modificarBD($articulo);
        }else{
            $this->nuevoEnArchivo($articulo);
        }
    }
    
    function eliminar(){
        $id = $_POST['id'];
        if(Controlador::$bd){
            $this->eliminarBD($id);
        }else{
            $this->borrarArchivo($id);
        }
    }
    
    function borrarArchivo($id){
        $nombre = "articulos/" . $id . ".dat";
        if(file_exists($nombre)){
            unlink($nombre);
            header('Location: blog.php');
        }
    }
    
    function getAllArticulos(){
        $articulos = array();
        if(Controlador::$bd){
            $sentencia = $this->conn->prepare("Select id_articulo, titulo, imagen,estado from t_articulo" );
            $sentencia->execute();
            $art = $sentencia->fetchAll();
            foreach($art as $f){
                $a = new Articulo();
                $a->id= $f["id_articulo"];
                $a->titulo= $f["titulo"];
                $a->imagen= $f["imagen"];
                $a->activo=$f["estado"];
                $articulos[] = $a;
            }
            return $articulos;
        }else{
            $files = scandir('articulos/');
            foreach($files as $f){
                $archivo = fopen('articulos/'.$f,"r");
                if($archivo!=null and $f!="." and $f!=".."){
                    $articulo = new Articulo();
                    $articulo->id = str_replace(".dat","",$f);
                    $articulo->fecha = fgets($archivo);
                    $articulo->titulo = fgets($archivo);
                    $articulo->descripcion = fgets($archivo);
                    $articulo->imagen  = fgets($archivo);
                    $articulos[] = $articulo;
                    fclose($archivo);
                }
            }
            return $articulos; 
        }
        
    }
    
    function getArticuloPorId($id){
        $articulo = new Articulo();
        if(Controlador::$bd){
            $sentencia = $this->conn->prepare("Select id_articulo,fecha,titulo,descripcion, imagen,estado from t_articulo where id_articulo=?" );
            $sentencia->bindParam(1, $id);
            $sentencia->execute();
            $art = $sentencia->fetch();
            if($art==null){
                echo "<h1> El articulo solicitado: $id. no existe </h1>";
                $this->cerrarConexion();
                die("no encontre el articulo $id");
            }else{
                if($art["estado"]==false){
                    echo "<h1> El articulo solicitado: $id. fue borrado </h1>";
                    $this->cerrarConexion();
                    die("el articulo esta desactivado $id");
                }else{
                    $articulo->id=$id;
                    $articulo->fecha = $art["fecha"];
                    $articulo->titulo = $art["titulo"];
                    $articulo->descripcion = $art["descripcion"];
                    $articulo->imagen  = $art["imagen"];
                    $articulo->activo = $art["estado"];
                    
                    //HARDCODEADO PARA Q NO DEVUELVA LOS COMENTARIOS
                    $articulo->comentarios = NULL;
                    return $articulo;
                    
                    $sent = $this->conn->prepare("Select id_comentario, usuario,coment from t_comentario c where c.articulo = ?" );
                    $sent->bindParam(1,$id);
                    $sent->execute();
                    $coments = $sent->fetchAll();
                    $comentarios=null;
                    foreach($coments as $tupla){
                        $c = new Comentario();
                        $c->id = $tupla["id_comentario"];
                        $c->id_articulo= $id;
                        $c->usuario= $tupla["usuario"];
                        $c->coment = $tupla["coment"];
                        $comentarios[] = $c;
                    }
                    $articulo->comentarios = $comentarios;
                    
                    $this->cerrarConexion();
                    return $articulo;
                }
            }
            
        }else{
            if(file_exists("articulos/" . $id . ".dat")){
                $archivo = fopen("articulos/" . $id . ".dat", "r");
                $articulo->id = $id;
                $articulo->fecha = fgets($archivo);
                $articulo->titulo = fgets($archivo);
                $articulo->descripcion = fgets($archivo);
                $articulo->imagen  = fgets($archivo);
                fclose($archivo);
                return $articulo;
            }else{
                return null;
            }
        }
       
    }
    
    function nuevoEnBD($articulo){
        $sentencia = $this->conn->prepare("INSERT INTO t_articulo
        (fecha, titulo, descripcion, imagen, estado) VALUES (?, ?, ?, ?, ?)" );
        $sentencia->bindParam(1, $articulo->fecha);
        $sentencia->bindParam(2, $articulo->titulo);
        $sentencia->bindParam(3, $articulo->descripcion);
        $sentencia->bindParam(4, $articulo->imagen);
        $sentencia->bindParam(5, $articulo->activo);
        $sentencia->execute();
        header('Location: ' . 'verArticulo.php?id=' . $this->getLastID());
        $this->cerrarConexion();
    }
    
    function nuevoEnArchivo($articulo){
        $archivo = fopen("articulos/" . $articulo->id . ".dat" , "w+");
       
        if($archivo==null){
            echo "<h1> no pude abrir el archivo </h1>";
            die();
        }
        fwrite($archivo, $articulo->fecha. "\n");
        fwrite($archivo, $articulo->titulo . "\n" );
        fwrite($archivo, $articulo->descripcion . "\n");
        fwrite($archivo, $articulo->imagen . "\n");
        fclose($archivo);
        
        header('Location: ' . 'verArticulo.php?id=' . $articulo->id);
    }
    
    function modificarBD($articulo){
        $sentencia = $this->conn->prepare("UPDATE t_articulo 
        SET fecha=?, titulo=?, descripcion=?, imagen=?
        WHERE id_articulo=?" );
        $sentencia->bindParam(1, $articulo->fecha);
        $sentencia->bindParam(2, $articulo->titulo);
        $sentencia->bindParam(3, $articulo->descripcion);
        $sentencia->bindParam(4, $articulo->imagen);
        $sentencia->bindParam(5, $articulo->id);
        $sentencia->execute();
        header('Location: ' . 'verArticulo.php?id=' . $articulo->id);
        $this->cerrarConexion();
    }
    
    function eliminarBD($id){
        $sentencia = $this->conn->prepare("UPDATE t_articulo SET estado=false WHERE id_articulo=?" );
        $sentencia->bindParam(1, $id);
        $sentencia->execute();
        header('Location: blog.php');
        $this->cerrarConexion();
    }
    
    function nuevoComentario(){
        $c = new Comentario();
        $c->id_articulo = $_POST["id"];
        $c->usuario = $_POST["usuario"];
        $c->coment = $_POST["comentario"];
        $sentencia = $this->conn->prepare("INSERT INTO t_comentario(usuario, coment, articulo)VALUES (?, ?, ?) " );
        $sentencia->bindParam(1, $c->usuario);
        $sentencia->bindParam(2, $c->coment);
        $sentencia->bindParam(3, $c->id_articulo);
        $sentencia->execute();
        $this->cerrarConexion();
        if(! isset($_POST["comentarios"])){
             //header('Location: verArticulo.php?id=' . $c->id_articulo);
        }
       
    }
    
    function eliminarComentario(){
        $id = $_POST["id_comentario"];
        $sentencia = $this->conn->prepare("DELETE FROM t_comentario WHERE id_comentario=? " );
        $sentencia->bindParam(1, $id);
        $sentencia->execute();
        $this->cerrarConexion();
        header('Location: verArticulo.php?id=' . $_POST["id_articulo"] );
    }
    
    function cerrarConexion(){
        $this->conn=null;
    }
    
    function getAllComentarios(){
        $id = $_GET["idArticulo"];
        $sent = $this->conn->prepare("Select id_comentario, usuario,coment from t_comentario c where c.articulo = ?" );
        $sent->bindParam(1,$id);
        $sent->execute();
        $coments = $sent->fetchAll();
        $comentarios=null;
        foreach($coments as $tupla){
            $c = new Comentario();
            $c->id = $tupla["id_comentario"];
            $c->id_articulo= $id;
            $c->usuario= $tupla["usuario"];
            $c->coment = $tupla["coment"];
            $comentarios[] = $c;
        }
        $this->cerrarConexion();
        return $comentarios;
    }
    
}
?>