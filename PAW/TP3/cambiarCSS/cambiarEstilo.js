var change = function(){
    var s= document.getElementById("select-css");
    var nombre;
    if( s.value == 1){
        nombre="blanco.css";
    }else{
        nombre="oscuro.css";
    }
    document.getElementById("fondo").setAttribute("href",nombre)
}