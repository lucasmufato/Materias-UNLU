var memo;

window.onload = function () {
    memo = new Memotest();
};

function Memotest () {
    
    this.jugadores = null; //para saber la cantidad de jugadores
    this.nivel = 1; //nivel actual
    this.nivelfin = 6; //nivel al que termina el juego
    this.seleccionada = null;   //guardo el primer click q hace
    this.cartas = []; //arreglo con las cartas
    this.turno = 0;
    this.nombres=[];   //arreglo con los nombres de el/los jugadores
    this.encontradas=[]; // arreglo con los pares ya encontrados
    
    this.setJugadores = function (nro) {
        this.jugadores = nro;
        var div = document.getElementById("pedir_nombres");
        div.innerHTML = "";
        var label1 = document.createElement("label");
        label1.innerHTML= "Nombre jugador 1:" ;
        var input1 = document.createElement("input");
        input1.setAttribute("type", "text");
        input1.setAttribute("id", "nombre1");
        div.appendChild(label1);
        div.appendChild(input1);
        if (nro === 2) {
            var label2 = document.createElement("label");
            label2.innerHTML="Nombre jugador 2:";
            var input2 = document.createElement("input");
            input2.setAttribute("type", "text");
            input2.setAttribute("id", "nombre2");
            div.appendChild(label2);
            div.appendChild(input2);
        }
        var button = document.createElement("button");
        button.setAttribute("onclick" , "memo.agregarNombres()");
        button.innerHTML= "Comenzar!" ;
        div.appendChild(button);
    };
    
    this.agregarNombres = function(){
        var n1 = document.getElementById("nombre1").value;
        var t = document.getElementById("tabla");
        var row1= document.createElement("tr");
        var th = document.createElement("th");
        th.innerHTML= n1;
        row1.appendChild(th);
        this.nombres.push(n1);
        if(this.jugadores === 2){
            var n2 = document.getElementById("nombre2").value;
            var th2= document.createElement("th");
            th2.innerHTML = n2;
            row1.appendChild(th2);
            this.nombres.push(n2);
        }
        t.appendChild(row1);
        var row2 = document.createElement("tr");
        var punto1 = document.createElement("td");
        punto1.setAttribute("id","puntos_jugador_1");
        punto1.innerHTML = "0";
        row2.appendChild(punto1);
        if(this.jugadores === 2){
            var punto2 = document.createElement("td");
            punto2.innerHTML = "0";
            punto2.setAttribute("id","puntos_jugador_2");
            row2.appendChild(punto2);
        }
        t.appendChild(row2);
        this.mostrarTurno();
        
        //hacer invisible la donde pido datos de usuarios
        var se = document.getElementById("cantidad");
        se.setAttribute("style","display: none");
        
        this.armarTablero();
    };
    
    this.mostrarTurno = function(){
        var t = document.getElementById("turno");
        t.innerHTML ="Turno de:  "+ this.nombres[this.turno];
        console.log("tunro de: "+this.nombres[this.turno]);
    };
    
    this.armarTablero = function(){
        var seccion = document.getElementById("juego");
        seccion.innerHTML = "";
        
        if(this.nivel === this.nivelfin){
            alert("terminaron el juego! ");
        }else{
            this.encontradas= [];
            this.randomizarCartas(this.nivel+3);
            if(this.nivel !== 1){
                alert("pasaste de nivel! :D");
            }
        }
        
        //creo un UL y por cada img un LI
        var ul = document.createElement("ul");        
        var p;
        for( p in this.cartas ){
            var li = document.createElement("li");
            li.setAttribute("onClick","memo.tocoCarta("+p+")");
            
            var i = document.createElement("img");
            i.setAttribute("src","img/"+this.cartas[p]+".jpg");
            i.setAttribute("onClick","memo.tocoCarta("+p+")");
            i.setAttribute("id",p);
            
            li.appendChild(i);
            ul.appendChild(li);
        }
        seccion.appendChild(ul);
        
    };

    this.randomizarCartas = function(nro){
        var cartasOrdenadas = [];
        //por cada nro de cartas agrego un par a la lista
        for(var i=0;i<=nro;i++){
            cartasOrdenadas.push(i);
            cartasOrdenadas.push(i);
        }
        
        this.cartas = cartasOrdenadas.sort(function(a, b){return 0.5 - Math.random()});
        console.log(cartasOrdenadas);
    };
    
    this.tocoCarta = function(nro){
        
        //si la carta de la imagen esta entre las encontrada no hago nada
        if( this.encontradas.includes( this.cartas[nro] ) ){
            console.log("esta imagen ya fue encontrada!");
            console.log(this.encontradas);
            return ;
        }
        
        var imagen = document.getElementById(nro);
        if( this.seleccionada === null){
            //si es la primer carta que toca la muestro y guardo el id
            this.seleccionada = nro;
            imagen.classList.add("visible");
            imagen.classList.add("seleccionada");
        }else{
            if(this.seleccionada !== nro){
                //si es la segunda carta que toca, la muestro y comparo si son del mismo tipo
                imagen.classList.add("visible");
                if ( this.cartas[ nro ] === this.cartas[ this.seleccionada] ){
                    //si tiene el mismo numero entonces el usuario le pego a 2 iguales
                    //saco la seleccion
                    document.getElementById(this.seleccionada).classList.remove("seleccionada");
                    this.seleccionada = null;
                    this.encontradas.push(this.cartas[nro]);
                    
                    //sumo los puntos
                    var tur = this.turno+1;
                    var td = document.getElementById( "puntos_jugador_"+ tur );
                    var puntos =parseInt( td.innerHTML );
                    puntos+=1;
                    td.innerHTML = puntos;
                    
                    //paso turno
                    this.pasarTurno();
                    
                    //compruebo si se termino el nivel
                    if(this.encontradas.length*2 >= this.cartas.length){
                        this.nivel+=1;
                        this.armarTablero();
                    }
                    
                }else{
                    //si tiene distinto numero, dejo q las vea por un cachito y desp las escondo
                    setTimeout(function(){
                            imagen.classList.remove("visible");
                            //la otra carta que era visible tamb la escondo
                            document.getElementById(memo.seleccionada).classList.remove("visible");
                            document.getElementById(memo.seleccionada).classList.remove("seleccionada");
                            memo.seleccionada = null;
                        }, 2000);
                    this.pasarTurno();
                }
            }
        }
    }; // fin metodo tocoCarta
    
    this.pasarTurno = function(){
        if(this.jugadores > 1){
            this.turno+=1;
            if(this.turno >= this.jugadores){
                this.turno = 0;
            }
            this.mostrarTurno();
        }else{
            console.log("jugando solo, seguis vos..");
        }
    };
}