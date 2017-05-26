<?php

include_once "Comentario.php";

class BaseDatos{
    private $bd_name="parcialmufato";
    private $bd_host="localhost";
    private $bd_port=5432;
    private $bd_user="lucas";
    private $bd_pass="lucas";
    private $conn;
    
    function __construct(){
    }
    
    function conectarse(){
        $this->conn = new PDO("pgsql:host=$this->bd_host;dbname=$this->bd_name", $this->bd_user, $this->bd_pass);
        $this->conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        return true;
    }
    
    function nuevoComentario($nombre,$mail,$msj){
        $prep = $this->conn ->prepare("INSERT INTO comentarios(nombre, mail, msj)VALUES (?, ?, ?)");
        $prep-> bindParam(1,$nombre);
        $prep-> bindParam(2,$mail);
        $prep-> bindParam(3,$msj);
        $prep->execute();
        $this->conn = null;
        return true;
    }
    
    function getComentarios($mail){
        $prep = $this->conn ->prepare("SELECT nombre,msj from comentarios where mail = ?");
        $prep-> bindParam(1,$mail);
        $prep-> execute();
        $rta = $prep->fetchAll();
        $coments= array();
        foreach($rta as $tupla){
            $c = new Comentario();
            $c->nombre= $tupla['nombre'];
            $c->msj= $tupla['msj'];
            $coments[] = $c;
        }
        $this->conn=null;
        return $coments;
    }
    
}
?>