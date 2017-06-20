<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Mufa's blog</title>
    <link rel="stylesheet" href="../css/blog_articulo.css">
    <link href="https://fonts.googleapis.com/css?family=Ravi+Prakash" rel="stylesheet">
    <script type="application/javascript" src="../../jquery-3.2.1.min.js"></script>
    <script type="application/javascript" src="articulo.js"></script>
    
</head>
<body>
<?php
    include_once "Controlador.php";
    include_once "Articulo.php";
    include_once "Comentario.php";
    /*
        CHEQUEOS VARIOS
    */
    if($_SERVER["REQUEST_METHOD"] == "POST"){
        echo "<h1> Error! vuelva a <a href='blog.php'>blog</a> </body> </html>";
        die();
    }
    $id=$_GET["id"];
    if($id==null){
        echo "<h1> Error falta el articulo a ver! vuelva a <a href='blog.php'>blog</a> </body> </html>";
        die();
    }
    $controlador = new Controlador();
    $articulo = $controlador->getArticuloPorId($id);
    if($articulo==null){
        echo "<h1> El articulo no existe! :( <br/> vuelva a <a href='blog.php'>blog</a> </body> </html>";
        die();
    }
    echo "<h1> $articulo->titulo </h1>";
?>
   
    <section id='cuerpo'>
    <div>
    <a href="blog.php" id="volver">Volver</a>
    
<?php
    echo "<p id='fecha'> $articulo->fecha </p>";
    echo "</div>";
    if($articulo->imagen !=null and $articulo->imagen !="\n"){
        echo "<img src='../imagenes/"."$articulo->imagen'>";
    }
    echo "<pre> $articulo->descripcion </pre>";
?>
    </section>
    <section id='comentarios'>
    <h5> Comentarios: </h5>
    <ul id='lista_comentarios'>
<?php
    if($articulo->comentarios!=null){
       foreach($articulo->comentarios as $c){
        echo "<li class='li_comentario' >";
        echo "<p class='p_comentario_usuario' >";
        if( $c->usuario == null or $c->usuario == ""){
            echo "anonimo";
        }else{
            echo $c->usuario;
        }
        echo "</p>";
        echo "<p class='p_comentario_coment' > $c->coment </p>";
        echo "<form id='f_nuevo_comentario' action='dispacher.php' method='post' enctype='multipart/form-data'>";
        echo "  <input type='hidden' name='id_comentario' value='$c->id'> ";
           echo "  <input type='hidden' name='id_articulo' value='$articulo->id'> ";
        echo "  <input type='submit' value='x' name='operacion'>";
        echo "</form>";
        echo "</li>";
        } 
    }else{
        echo "<p> No hay comentarios </p>";
    }
    
?>
    </ul>
    <form id="f_nuevo_comentario">
<?php 
        echo " <input type='hidden' name='id' id='idArticulo' value='$articulo->id'> ";
?>        
        <label for="i_usuario" > usuario: </label>
        <input id="i_usuario" type="text" name="usuario" max="30">
        <textarea type="text" name="comentario" min="5" max="300" placeholder="comentario..." required id="i_coment"></textarea>
        <button value="nuevo comentario" name="operacion" id="nuevoComentario">nuevo comentario</button>
    </form>
</section>
<section id='modificar'>
    <form id="f_nuevo_articulo" action="dispacher.php" method="post" enctype="multipart/form-data" >
        <?php 
            echo " <input type='hidden' name='id' value='$articulo->id'> ";
        ?>
        <label for="i_titulo">Titulo (max 50 caracteres)</label>
        <input id="i_titulo" type="text" name="titulo" min="5" max="50" required="true">
        <label for="i_descr">Descripcion (max 500 caracteres)</label>
        <textarea id="i_descr" type="text" name="descripcion" min="5" max="500" placeholder="ingrese la descripcion"></textarea>
        <label for="i_img">Desea subir una imagen?</label>
        <input id="i_img" type="file" name="img">
        <input type="submit" value="modificar" name="operacion">
    </form>
    <form id="eliminar" action="dispacher.php" method="post" enctype="multipart/form-data">
       
        <?php 
            echo " <input type='hidden' name='id' value='$articulo->id'> ";
            echo '<input type="submit" name="operacion" value="eliminar" >';
        ?>
    </form>
</section>
</body>
</html>