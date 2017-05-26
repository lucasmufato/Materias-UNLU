function agregarItem() {
  var item = document.createElement("article");
  var accion = document.forms["nuevoItem"].accion.value;
  var descripcion = document.forms["nuevoItem"].descripcion.value;

  var desc = document.createElement("p");
  var tdesc = document.createTextNode(descripcion);
  desc.appendChild(tdesc);

  var haccion = document.createElement("h3");
  haccion.setAttribute("class", "item");
  var taccion = document.createTextNode(accion);
  haccion.appendChild(taccion);

  item.appendChild(haccion);
  item.appendChild(desc);

  var prioridad = document.getElementsByName("prioridad");
  var p = "";
  for (var i = 0; i < prioridad.length; i++) {
    if (prioridad[i].checked) {
      p = prioridad[i].value;
    }
  }
  if (p !== "") {
    document.getElementsByClassName(p)[0].appendChild(item);
  } else {
    alert("Por favor elija prioridad");
  }
}
