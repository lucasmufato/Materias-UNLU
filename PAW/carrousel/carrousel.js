window.onload = function(){
	//sigo bastante el ejemplo del paint
	var appcarrousel = new carrousel()
	appcarrousel.inicializar();

	//manejo los clicks de las flechitas
	$(document).ready(function(){
   		 $("#carrousel-sig").click(function(){
      		  appcarrousel.siguiente();
   		 });
   		 $("#carrousel-ant").click(function(){
      		  appcarrousel.anterior();
   		 });
	});
	console.log(appcarrousel);
}

var carrousel = function(){
	//parte de "configuracion"
	this.id_div="carrousel";			//id q tiene el div en el q aparece el carrousel
	this.id_ul_img="carrousel-ul-img";		//id que va a tener el ul q tiene las imagenes
	this.id_ul_puntitos="carrousel-ul-p"; 		//id que va a tener el ul q tiene los puntitos
	this.class_img="carrousel-img";			//clase q van a tener las imagenes	
	this.class_p="carrousel-p";			//clase q van a tener los puntitos
	this.maximo=5;	//maxima cantidad de imagenes y de puntitos


	this.contenedor= document.getElementById(this.id_div);		//obtengo ese objeto mediante el id definido
	this.imagenes = new Array();		//arreglo con las imagenes
	this.puntitos = new Array();			//arreglo con los puntitos para cambiar de imagen
	this.flechaSiguiente = new flecha("anterior",this,this.contenedor);
	this.flechaAnterior = new flecha("siguiente",this,this.contenedor);
	this.actual=0;

	this.inicializar = function(){
		//creo el ul en el que se encuentran las imagenes y le pongo el id predefinido
		var ul_i=document.createElement("ul");
		ul_i.setAttribute("id",this.id_ul_img);
		
		// inicializar el vector con las imagenes
		for (var i = 0; i <this.maximo; i++) {
			this.imagenes[i]= new imagen(i,this);
			this.imagenes[i].create(ul_i);		
		}
		this.contenedor.appendChild(ul_i);
		//ya tengo la lista de las imagenes hecha.
		//ahora hago los puntitos, q es copiar y pegar mas que nada
		var ul_p=document.createElement("ul");
		ul_p.setAttribute("id",this.id_ul_puntitos);
		for (var i = 0; i <this.maximo; i++) {
			this.puntitos[i]= new punto(i,this); //hago un nuevo punto, le paso el numero q va a mostrar
												// y un puntero al carrousel
			this.puntitos[i].create(ul_p);
			
		}
		this.contenedor.appendChild(ul_p);
	}

	this.siguiente = function(){
		console.log("hiciste click en la flechita para adelante");
		console.log(this.imagenes)
		console.log(this.imagenes[this.actual])
		this.imagenes[this.actual].esconder();
		this.puntitos[this.actual].apagar();
		this.actual++;
		if (this.actual == this.maximo) {
			this.actual = 0;
		}
        console.log(this.actual);
		this.imagenes[this.actual].mostrar();
		this.puntitos[this.actual].prender();
	}

	this.anterior = function(){
		console.log("hiciste click en la flechita para atras");
		this.imagenes[this.actual].esconder();
		this.puntitos[this.actual].apagar();
		this.actual--;
		if (this.actual < 0) {
			this.actual = this.maximo-1;
		}
		this.imagenes[this.actual].mostrar();
		this.puntitos[this.actual].prender();
	}

	this.pasar_a_foto_nro= function(nro) {
		console.log("pasaste de la foto nro"+this.actual+" a la nro: "+nro);
		this.imagenes[this.actual].esconder();
		this.puntitos[this.actual].apagar();
		this.actual=nro;
		this.imagenes[this.actual].mostrar();
		this.puntitos[this.actual].prender();
	}
}

var imagen = function(numero, puntero_carrousel){
	this.carrousel=puntero_carrousel;
	this.id=numero;
	this.img;
	this.create=function(ul_i){
		this.img=document.createElement("img");
		this.img.setAttribute("class",this.carrousel.class_img);
		var nombre_img= "../carrousel/slider-"+this.id+".png";
		this.img.setAttribute("src",nombre_img);
		this.img.setAttribute("alt","foto del carrousel");
		//this.img.style.display="none";
		var li= document.createElement("li");
		li.appendChild(this.img);
		ul_i.appendChild(li);
	}
	this.mostrar= function(){
		this.img.style.display="block";
	}

	this.esconder= function(){
		this.img.style.display="none";
	}
}

var flecha = function(string,puntero_carrousel,contenedor){
	this.carrousel=puntero_carrousel;
	var p= document.createElement("p");
	p.setAttribute("class","carrousel-flecha");
	var newContent;
	if(string=="siguiente"){
		newContent = document.createTextNode(">");
		p.setAttribute("id","carrousel-sig");
		//p.addEventListener("click", carrousel.siguiente);		//anda con jquery
	}else{
		newContent = document.createTextNode("<");
		//p.addEventListener("click", carrousel.anterior);		//anda con jquery
		p.setAttribute("id","carrousel-ant");
	}			
	p.appendChild(newContent);

	contenedor.appendChild(p);
}

var punto= function(numero, puntero_carrousel){
	this.carrousel=puntero_carrousel;
	this.id=numero;
	this.li;
	this.create=function(ul_p){
		this.li = document.createElement("li");
		this.li.setAttribute("class",this.carrousel.class_p);
		//li.setAttribute.innerHTML(i);		//no anda
		//li.innerHTML(i);					//tampoco anda
		var newContent = document.createTextNode(this.id);			
		this.li.appendChild(newContent);			//a cada li le pongo un numero adentro
		var tagLi = this;
        console.log(tagLi);
        this.li.onclick = function() { tagLi.carrousel.pasar_a_foto_nro(tagLi.id);};
		ul_p.appendChild(this.li);
	}

	this.apagar= function(){
		this.li.style.background.color="white";
		this.li.style.color="black";
	}

	this.prender=function(){
		this.li.style.background.color="black";
		this.li.style.color="red";
	}
}
