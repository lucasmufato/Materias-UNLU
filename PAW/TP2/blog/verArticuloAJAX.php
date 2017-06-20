<?php

include_once("Controlador.php");

if($_SERVER["REQUEST_METHOD"] == "POST"){
    
    /* TENGO Q LLAMAR CON ESTOS DATOS
    $c->id_articulo = $_POST["id"];
    $c->usuario = $_POST["usuario"];
    $c->coment = $_POST["comentario"]
    */
    
    $controlador = new Controlador();
    $controlador->nuevoComentario();
    $rta= Array("status" => "ok");
    echo json_encode($rta);
}else{
    $controlador = new Controlador();
    $coments = $controlador->getAllComentarios();
    $rta = Array("status" => "ok", "comentarios" => $coments);
    echo json_encode($rta);
}
