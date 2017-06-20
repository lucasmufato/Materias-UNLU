var url = "verArticuloAJAX.php";

$(document).ready(function(){
    $("#nuevoComentario").click(function(){
       nuevoComentario();
    });
    
    cargarComentarios();
});

cargarComentarios = function(){
    var data = {
        "idArticulo" : $("#idArticulo").val()
    };
    var funcion = function(data,status){
        if(status !== "success"){
            alert("No se pudo conectar con el servidor");
            return;
        }
        console.log(data);
        data = JSON.parse(data);
        switch (data.status){
            case "ok":
                mostrarComentarios(data.comentarios);
                break;
        }
        
    };
    $.get(url,data,funcion);
}

mostrarComentarios = function(comentarios){
    console.log("comentarios: "+comentarios);
    
    var i=0;
    for(i;i<comentarios.length;i++){
        agregarComentario( comentarios[i].usuario, comentarios[i].coment );
    }
}

agregarComentario = function(usuario, comentario){
    var listaComentarios = document.getElementById("lista_comentarios");
    console.log("cree un comentario")
    var li = document.createElement("li");
    li.classList.add("li_comentario");

    var user = document.createElement("p");
    user.innerHTML = usuario;
    user.classList.add("p_comentario_usuario");

    var coment = document.createElement("p");
    coment.innerHTML = comentario;
    coment.classList.add("p_comentario_coment");

    li.appendChild(user);
    li.appendChild(coment);
    listaComentarios.appendChild(li);
}

nuevoComentario = function(){
    var data = $("#f_nuevo_comentario").serialize();
    
    var funcion = function(data,status){
        if(status !== "success"){
            alert("No se pudo conectar con el servidor");
            return;
        }
        console.log(data);
        data = JSON.parse(data);
        switch (data.status){
            case "ok":
                var user = document.getElementById("i_usuario");
                var coment = document.getElementById("i_coment");
                agregarComentario( user.val() ,coment.val() );
                user.val("");
                coment.val("");
                break;
        }
        
    };
    $.post(url,data,funcion);
}