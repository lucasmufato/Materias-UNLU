<?php

include_once "BaseDatos.php";

if($_SERVER["REQUEST_METHOD"] != "POST"){
    echo "<h1>ha ocurrido un error, vuelva a la pagina principal!</h1>";
    echo "<h2> <a href='index.html'>Volver<a>";
    exit();
}

$nombre = $_POST["nombre"];
$mail = $_POST["mail"];
$msj= $_POST["msj"];
$error=false;

if($nombre==null or $nombre==""){
    $error=true;
    echo "<h1>Falta el nombre!</h1>";
}
if($mail==null or $mail==""){
    $error=true;
    echo "<h1>Falta el mail!</h1>";
}
if($msj==null or $msj==""){
    $error=true;
    echo "<h1>Falta el mensaje!</h1>";
}
if($error){
    echo"<h2> <a href='index.html'>VOLVER</a> al formulario </h2>";
    exit();
}
$bd = new BaseDatos();
$ok = $bd->conectarse();
if(!$ok){
    echo "<h1> Estimado profesor: no se pudo conectar a la BD </h1>";
    die();
}
$ok= $bd->nuevoComentario($nombre,$mail,$msj);
if($ok){
    echo "<h1>Los datos se guardaron safisfactoriamente</h1>";
}else{
    echo "<h1>Hubo un error al guardar los datos! :(</h1>";
}
 echo"<h2> <a href='index.html'>VOLVER</a> al formulario </h2>";
?>