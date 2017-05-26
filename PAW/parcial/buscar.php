<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>legajo: 117780</title>
    <link rel="stylesheet" href="estilo.css">
</head>
<body>
<header>
	<h1>Parcial de Lucas Mufato</h1>
	<nav>
	    <a href="#form">Buscar comentarios por mail</a>
        <a href="index.html">Ingresar un comentario</a>
	</nav>	
</header>
<section id="form">
   <h2>Buscador de comentarios por MAILS</h2>
    <form method="get" action="buscar.php">
        <label for="f_mail">MAIL</label>
        <input type="email" id="f_mail" name="mail" max="50" required="true">
        <input type="submit" value="Buscar">
    </form>
</section>
<section id="results">
    <h3> Resultados de la busqueda: </h3>
<?php
    include_once "BaseDatos.php";
    include_once "Comentario.php";
    
    $mail = $_GET['mail'];
    if($mail==null or $mail==""){
        echo "No has realizado ninguna busqueda";
    }else{
        $bd = new BaseDatos();
        $ok = $bd->conectarse();
        $com = $bd->getComentarios($mail);
        if($com == null){
            echo "<h4> No hay mensajes de $mail</h4>";
        }else{
            echo "<h4> Los comentarios son: </h4>";
            echo "<ul class='comentarios'>";
            foreach($com as $c){
                echo "<li class='coment'> ";
                echo "<p> $c->nombre </p>";
                echo "<p> $c->msj </ṕ>";
                echo "</li>";
            }
            echo "</ul>";
        }
    }
?>
</section>
<footer>
    <p>Mufato Lucas</p>
    <p>Legajo: 117780</p>
    <p  class="fecha">28/4/2017</p>
</footer>
</body>
</html>