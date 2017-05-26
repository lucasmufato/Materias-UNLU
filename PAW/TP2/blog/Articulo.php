<?php

class Articulo{
    var $id;
    var $fecha;
    var $titulo;
    var $descripcion;
    var $imagen;
    var $comentarios;
    var $activo; //solo para la BD
    
    function __construct(){
        //constructor vacio
    }
    
    function toString(){
        return $this->id . $this->titulo . $this->descripcion . $this->imagen . $this->comentarios . $this->activo;
    }
}
?>