<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>TP2 EJ10</title>
</head>
<body>
    <?php
    
    $target_dir = "imagenes/";
    $target_file = $target_dir . basename($_FILES["foto"]["name"]);
    
    $uploadOk = 1;
    $imageFileType = pathinfo($target_file,PATHINFO_EXTENSION);
    // Check if image file is a actual image or fake image
    if(isset($_POST["submit"])) {
        $check = getimagesize($_FILES["foto"]["tmp_name"]);
        if($check !== false) {
            $uploadOk = 1;
        } else {
            echo "<h1>File is not an image.</h1>";
            $uploadOk = 0;
        }
    }
    // Allow certain file formats
    if($imageFileType != "jpg" ) {
        echo "<h1>Sorry, only JPG files are allowed.</h1>";
        $uploadOk = 0;
    }
    // Check if $uploadOk is set to 0 by an error
    if ($uploadOk == 0) {
        echo "Sorry, your file was not uploaded.";
    // if everything is ok, try to upload file
    } else {
        
        if (move_uploaded_file($_FILES["foto"]["tmp_name"], $target_file)) { //si se guardo bien
            $nombre = basename( $_FILES["foto"]["name"]);
            //muestro original
            echo "<h1> Tu foto fue subida con exito </h1>";
            echo "<img src='$target_file'>";
            //saco ancho y alto de la foto original
            list($img_width,$img_height) = getimagesize($target_file);
            //creo nueva imagen con tañano fijo
            $im = @imagecreatetruecolor(100, 75);
            //obtengo la imagen
            $img_source = imagecreatefromjpeg($target_file);
            //copio de la imagen original a la nueva
            imagecopyresampled($im, $img_source, 0, 0, 0, 0, 100, 75, $img_width, $img_height);
            //guardo la nueva imagen
            imagejpeg($im,"imagenes/thumbs/".$nombre);
            //muestro
            echo "<h2> La miniatura es: </h2>";
            echo "<img src='imagenes/thumbs/".$nombre."'>";
        } else {
            echo "Sorry, there was an error uploading your file.";
        }
    }
    
    
    ?>
</body>
</html>