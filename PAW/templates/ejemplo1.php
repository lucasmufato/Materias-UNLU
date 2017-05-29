<?php

include('MiVista.php');
$templates = new MiVista();
$templates->nombres = ['juan','maria','carlos','ana'];

$templates->render('index.phtml');
