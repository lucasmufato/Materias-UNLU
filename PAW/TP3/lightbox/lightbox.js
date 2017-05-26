var light;

window.onload = function () {
    light = new Lightbox();
    light.instanciar();
};

function Lightbox(){
   
    this.listas = [];       //para tener q un mismo lightbox muestre diferentes conjuntos de imagenes
    this.estado = false;       //para saber si se instancio bien o no.
    
    this.listaActual = null;
    this.imagenesActuales = [];
    this.actual = 0;
    
    this.instanciar = function(){
        this.listas = document.querySelectorAll('[data-lightbox-container]');
        if(this.listas.length <= 0){
            console.log("ERROR! no hay objeto con la clase data-lightbox-container");
            this.estado = false;
            return ;
        }
        console.log(this.listas);
        var l;
        for(l=0;l<this.listas.length;l++ ){
            var listaImagenes = this.listas[l].getElementsByTagName("img");
            if(listaImagenes.length <= 0){
                console.log("CUIDADO! el "+(l+1)+"° objeto lightbox NO tiene imagenes adentro");
            }
            var i;
            for(i=0;i<listaImagenes.length;i++){
                listaImagenes[i].setAttribute("onclick","light.mostrarImagen("+l+","+i+")");
            }
        }
        this.crearContenedor();
        this.estado=true;
    };
    
    this.crearContenedor = function(){
        var body = document.getElementsByTagName("body");
        body = body[0];
        
        //contenedor donde va un div con la imagen grande y las flechitas y la lista de otras imagenes
        var contenedor = document.createElement("section");
        contenedor.setAttribute("id","lightbox-section-container");
        contenedor.setAttribute("class","invisible");
        body.appendChild(contenedor);
        
        //contenedor de la imagen y flechitas
        var div = document.createElement("div");
        div.setAttribute("id","lightbox-div");
        contenedor.appendChild(div);
        var img = document.createElement("img");
        img.setAttribute("id","lightbox-img");
        div.appendChild(img);
        
        var spanIzq = document.createElement("span");
        spanIzq.setAttribute("class","lightbox-arrow lightbox-previous");
        spanIzq.setAttribute("onclick","light.anterior()");
        spanIzq.innerHTML = "❮";
        div.appendChild(spanIzq);
        
         var spanDer = document.createElement("span");
        spanDer.setAttribute("class","lightbox-arrow lightbox-next");
        spanDer.setAttribute("onclick","light.siguiente()");
        spanDer.innerHTML = "❯";
        div.appendChild(spanDer);
        
        //contenedor de las imagenes siguientes/anteriores
        var ul = document.createElement("ul");
        ul.setAttribute("id","lightbox-ul");
        contenedor.appendChild(ul);
        
    };
    
    this.mostrarImagen = function(lista, imagen){
        if(this.estado === false){
            console.log("no se muestra el modal por no se creo bien el objeto");
            return;
        }
        if(this.listaActual !== lista){
            this.armarLightbox(lista);
        }
        this.apuntarA(imagen);
        this.mostrarLightbox();
    };
    
    this.armarLightbox = function(lista){
        this.imagenesActuales = this.listas[lista].getElementsByTagName("img");
        var index;
        var ul = document.getElementById("lightbox-ul");
        for(index=0;index<this.imagenesActuales.length;index++){
            //por cada imagen de ese grupo creo un LI
            var li = document.createElement("li");
            li.setAttribute("class","lightbox-li");
            ul.appendChild(li);
            
            //le pongo la imagen con el source que dice el atributo especifio u el original si no tiene
            var nueva_img = document.createElement("img");
            var path = this.imagenesActuales[index].getAttribute("data-lightbox-image");
            if( path == "null"){
                path = this.imagenesActuales[index].getAttribute("src");
            }
            nueva_img.setAttribute("src",path);
            nueva_img.setAttribute("class","lightbox-imagenes");            
            li.appendChild( nueva_img );
            
        }
    };
    
    this.apuntarA = function(imagen){
        
    };
    
}