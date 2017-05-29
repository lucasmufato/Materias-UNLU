<?php

include_once ("vendor/autoload.php");

class BasicSite{
    private $web;
    
    function __construct(){
        $this->web = new Smary();
    }
    
    private function cuerpo(){
        $this->web->assign("cuerpo","<h2>Contenido Principal</h2>");
    }
    
    private function pie(){
        $this->web->assign("pie","Pie de pagina");
    }
    
    private function contenido(){
        $personas = array(  ['nombre' => 'Carlos', 'apellido' => 'Gomez'],
                            ['nombre' => 'ana', 'apellido' => 'rodriguez']);
        
        $this->web->assign('nombres',$personas);
    }
    
    public function crearWeb() {
        $this->cuerpo();
        $this->contenido();
        this->pie();
        $this->web->assign("ejemplo2.tpl");
    }
    
}

$pagina = new BasicSite();
$pagina->crearWeb();