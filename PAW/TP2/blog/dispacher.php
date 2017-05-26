<?php
$pag = "localhost/PAW/TP2/blog/blog.php";

include_once "Controlador.php";

if($_SERVER["REQUEST_METHOD"] != "POST"){
         header('Location: '.$pag);
}

$var = $_POST['operacion'];
$controlador = new Controlador();
switch ($var){
    case "nuevo":
        $controlador->nuevo();
        break;
    case "modificar":
        $controlador->modificar();
        break;
    case "eliminar":
        $controlador->eliminar();
        break;
    case "nuevo comentario":
        $controlador->nuevoComentario();
        break;
    case "x":
        $controlador->eliminarComentario();
        break;
    default:
        header('Location: '.$pag);
        break;
}


?>