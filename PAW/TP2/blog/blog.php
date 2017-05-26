<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Mufa's blog</title>
    <link rel="stylesheet" href="../css/blog_index.css">
</head>
<body>
    <h1>Bienvienido al blog de Lucas Mufato</h1>
    <section id="seccion_principal">
    <aside>
        <h2>Articulos Destacados</h2>
        <ul id="lista_articulos">
        <?php
            include_once "Controlador.php";
            include_once "Articulo.php";
            $controlador = new Controlador();
            $articulos = $controlador->getAllArticulos();
            foreach($articulos as $a){
                if($a->activo){
                    echo "<li class='articulo'>";
                    echo "<a href='verArticulo.php?id=". $a->id ."' > ". $a->titulo ."</a>";
                    if(isset($a->imagen) and $a->imagen!=null and $a->imagen!="\n"){
                        echo "<img src='../imagenes/thumbs/". $a->imagen . "'>";
                    }
                    echo "</li>";
                } 
            }

        ?>
        </ul>
    </aside>
    <article class="articulo" id="nuevo_articulo"> 
        <h3> Nuevo Articulo  </h3> 
        <form id="f_nuevo_articulo" action="dispacher.php" method="post" enctype="multipart/form-data" >
            <label for="i_titulo">Titulo (max 50 caracteres)</label>
            <input id="i_titulo" type="text" name="titulo" min="5" max="50" required="true">
            <label for="i_descr">Descripcion (max 500 caracteres)</label>
            <textarea id="i_descr" type="text" name="descripcion" min="5" max="500" placeholder="ingrese la descripcion"></textarea>
            <label for="i_img">Desea subir una imagen?</label>
            <input id="i_img" type="file" name="img">
            <input type="submit" value="nuevo" name="operacion" id="i_submit">
        </form>
    </article>
    </section>
</body>
</html>