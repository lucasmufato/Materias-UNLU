<?php   

class MiVista{
    protected $templateDir = '';
    protected $vars = [];
    
    public function __contruct($templateDir = null){
        if ( ! is_null($templateDir)){
            $this->templateDir = $templateDir;
        }
    }
    
    public function render($templateFile){
        if ( file_exists( $this->templateDir . $templateFile ) )
            include $this->templateDir . $templateFile;
        else
            throw new exception("no existe el template $this->templateFile en la carpeta $this->templateDir");
    }
    
    public function __set($name, $value){
        $this->vars[$name] = $value;
    }
    
    public function __get($name){
        return $this->vars[$name];
    }
}
?>