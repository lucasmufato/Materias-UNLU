
window.setInterval(function(){
    var xhttp = new XMLHttpRequest();
    
    xhttp.onreadystatechange = function() {
        //uso this por q cuando se llame el evento estoy dentro del objeto xmlhttprequest
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("time").innerHTML = this.responseText;
       }else{
           if(this.readyState == 4 && this.status != 200){
               document.getElementById("time").innerHTML = "error en la comunicacion con el servidor";
           }
       }
    };
    xhttp.open("GET", "tiempo.php", true);
    xhttp.send();
    
    
    
}, 1000);