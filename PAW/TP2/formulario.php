<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>TP2 EJ8</title>
    <link rel="stylesheet" href="css/formulario.css">
</head>
<body>
    <h1>Formulario para pedir turnos</h1>
    <form action='mostrarFormulario.php' method="post">
    <label for='input_tipo'>Tipo</label>
    <select name='tipo' id="input_tipo">
    
    <?php
        $titulos = array('Sr','Sra','Dr');
        foreach ($titulos as $t){
            echo "<option value='$t'>$t</option>";
        }
    ?>
    
    </select>
    <label for="input_nombre">Nombre:</label>
    <input type="text" name="nombre" min="3" max="50">
    <label for="input_mail">Email:</label>
    <input type="email" name="email" id="input_email" min="5" max="50">
    <label for="input_tel">Telefono:</label>
    <input type="text" name="telefono" id="input_tel" min="5" max="50">
    <label for="input_edad">Edad:</label>
    <input type="number" name="edad" id="input_edad" max="110" min="1">
    <label for="input_calzado">Talla de calzado:</label>
    <input type="number" name="calzado" id="input_email" min="20" max="45">
    <label for="input_altura">Altura(CM):</label>
    <input type="range" name="altura" id="input_altura" min="30" max="220">
    <label for="input_nacimiento">Fecha de Nacimiento:</label>
    <input type="date" name="fecha" id="input_nacimiento" min="1910-1-1" max="2017-1-1">
    <label for="input_pelo">Color de Pelo:</label>
    <input type="color" name="pelo" id="input_color">
    <label for="input_horario">Horario del turno:</label>
    
    <input list="horario" name="horario" id="input_horario">
        <datalist id="horario">
    <?php
        $inicio=8;
        $fin=17;
        for($i=$inicio;$i<$fin;$i++){
           for($m=0;$m<60;$m=$m+15){
               echo "<option value='$i:$m' />";
           }
        }    
    ?>
    </datalist>
    <div class="contenedor">
        <input type="submit" class="boton" id="submit">
        <input type="reset" class="boton" id="reset">
    </div>
    </form>
</body>