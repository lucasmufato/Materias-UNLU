<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>TP2 EJ9</title>
    <link rel="stylesheet" href="css/formulario.css">
</head>
<body>
   
    <?php
        $variables= array("tipo","nombre","email","telefono","edad","calzado","altura","fecha","pelo","horario");

        $bd=true;
        if($bd){
            try {
                
                $username ="lucas";
                $password ="lucas";
                
                $conn = new PDO("pgsql:host=localhost;dbname=PAW", $username, $password);
                // set the PDO error mode to exception
                $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
                
                $insert = "INSERT INTO turno (tipo,nombre,email,telefono,edad,calzado,altura,fecha,pelo,horario) VALUES (";
                foreach($variables as $v){
                    $insert = $insert . "'" . $_POST[$v] ."'," ;
                }
                $insert = $insert . ",";
                $newInsert=rtrim($insert,",,");
                $newInsert = $newInsert . ");";
                //echo "el Stament me quedo como <br/>";
                //echo $newInsert;
                $rta =$conn->exec($newInsert);
                //echo "<br/>". $rta;
                $last_id = $conn->lastInsertId();
                echo "<h2> su turno es el nro: $last_id </h2>";
                echo "<h3> Los datos en la BD quedan: </h3>";
                
                $sql = 'SELECT * FROM turno where nro='.$last_id;
                $rta = $conn->query($sql);
                
                $nro =0;
                foreach($rta as $r){
                    foreach ($variables as $v) {
                        echo "<p> $v: " .$r[$v] ." </p>";
                    }
                }
                
                $conn=null;
                }catch(PDOException $e){
                    echo "<h1>Connection failed: " . $e->getMessage() . "</h1>";
                }
        }else{
           
            echo "<h1>La respuesta fue:</h1>";
            if ($_SERVER["REQUEST_METHOD"] == "POST"){
                foreach($variables as $v){
                    echo "<p> $v: $_POST[$v] </p>";
                }
            }else{
                foreach($variables as $v){
                    echo "<p> $v: $_GET[$v] </p>";
                }
            } 
        }
        
        
    ?>
</body>
</html>