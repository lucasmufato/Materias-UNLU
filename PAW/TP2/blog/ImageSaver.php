<?php

    class ImageSaver{
    
        static function guardarImagen(){
            $target_dir = "../imagenes/";
            $nombre = basename($_FILES["img"]["name"]);
            if($nombre==null){
                return null;
            }
            $target_file = $target_dir . $nombre;
            
            $uploadOk = 1;
            $imageFileType = pathinfo($target_file,PATHINFO_EXTENSION);
            // Check if image file is a actual image or fake image
            $check = getimagesize($_FILES["img"]["tmp_name"]);
            
            if($check !== false) {
                $uploadOk = 1;
            } else {
                echo "<h1> error! 1 </h1>";
                return null;
            }
            
            // Allow certain file formats
            if($imageFileType != "jpg" ) {
                echo "<h1> error! 2 </h1>";
                return null;
            }
            
            // Check if $uploadOk is set to 0 by an error
            if ($uploadOk == 0) {
                echo "<h1> error! 3 </h1>";
                return null;
            // if everything is ok, try to upload file
            } else {
                if (move_uploaded_file($_FILES["img"]["tmp_name"], $target_file)) { //si se guardo bien
                    
                    $nombre = basename( $_FILES["img"]["name"]);
                    //saco ancho y alto de la img original
                    list($img_width,$img_height) = getimagesize($target_file);
                    //creo nueva imagen con tañano fijo
                    $im = @imagecreatetruecolor(100, 75);
                    //obtengo la imagen
                    $img_source = imagecreatefromjpeg($target_file);
                    //copio de la imagen original a la nueva
                    imagecopyresampled($im, $img_source, 0, 0, 0, 0, 100, 75, $img_width, $img_height);
                    //guardo la nueva imagen
                    imagejpeg($im,"../imagenes/thumbs/".$nombre);
                    echo "<h1> mande la imagen $nombre </h1>";
                    return $nombre;
                    
                } else {
                    echo "<h1> error! 4 </h1>";
                    return null;
                }
            }
        }
    }
?>