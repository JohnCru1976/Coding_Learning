const container_show_image = document.getElementById("container_show_image");


const show_point = document.getElementById("show_point");

const coordinates = document.getElementById("coordinates");

const puntosLista = document.getElementById("puntos-lista");
const buscarInput = document.getElementById("buscar");

// **********
// Inicio
// **********
// Este código se ejecutará una vez que se haya cargado completamente el DOM
document.addEventListener("DOMContentLoaded", function() {
    mostrar_ventana(0)  // Cambiar a 2 para acceder a modo ubicar punto ... 0 para mostrar pantalla inicial
  });

  function mostrar_ventana(num) {
    // Declaración de todas las ventanas disponibles
    const test_image = document.getElementById("test_image")
    const show_image = document.getElementById("show_image")
    const list_places = document.getElementById("list_places")
    const updates = document.getElementById("updates")
    const new_point = document.getElementById("new_point")
    const edit_point = document.getElementById("edit_point")
    if (num == 0) {
      list_places.style.display = "block"; 
      show_image.style.display = "none";
      test_image.style.display = "none";
      updates.style.display = "none"
      new_point.style.display = "none"
      edit_point.style.display = "none"
    }
    if (num == 1) {
      list_places.style.display = "none"; 
      show_image.style.display = "block";
      test_image.style.display = "none";
      updates.style.display = "none"
      new_point.style.display = "none"
      edit_point.style.display = "none"
    }
    if (num == 2) {
      list_places.style.display = "none"; 
      show_image.style.display = "none";
      test_image.style.display = "block";
      updates.style.display = "none"
      new_point.style.display = "none"
      edit_point.style.display = "none"
    }
    if (num == 3) {
      list_places.style.display = "none"; 
      show_image.style.display = "none";
      test_image.style.display = "none";
      updates.style.display = "block"
      new_point.style.display = "none"
      edit_point.style.display = "none"
    }
    if (num == 4) {
      list_places.style.display = "none"; 
      show_image.style.display = "none";
      test_image.style.display = "none";
      updates.style.display = "none"
      new_point.style.display = "block"
      edit_point.style.display = "none"
      new_x = 50
      new_y = 50
      showPoint_new({x_percentage: new_x, y_percentage: new_y});
    }
    if (num == 5) {
      list_places.style.display = "none"; 
      show_image.style.display = "none";
      test_image.style.display = "none";
      updates.style.display = "none"
      new_point.style.display = "none"
      edit_point.style.display = "block"
    }
  }

  // El usuario pulsa el botón "atrás" en el navegador.
  window.addEventListener('popstate', function(event) {
    handleClick()
  });

// *************************************************************
// Muestra el listado inicial y un cuadro de búsqueda
// *************************************************************
const showBackButton = document.getElementById("show_back");
showBackButton.addEventListener("click", handleClick);
buscarInput.addEventListener("input", mostrarResultados);

mostrarResultados(); // Mostrar resultados iniciales

// Función que se llamará cuando se haga clic en el botón
function handleClick() {
    mostrar_ventana(0)
}

function mostrarResultados() {
    puntosLista.innerHTML = "";
    var filtro = quitarAcentos(buscarInput.value.toLowerCase());
    
    // Ordenar el array por la clave "text" de menor a mayor
    test_point.sort((a, b) => a.text.localeCompare(b.text));
    
    test_point.forEach(function(point, index) {
        var texto = quitarAcentos(point.text.toLowerCase());
        if (texto.includes(filtro)) {
            var listItem = document.createElement("li");
            listItem.style.fontSize = "50px";
            listItem.innerHTML = `<strong>${point.text}</strong>, ${point.building}, Planta: ${point.floor}`;
            listItem.setAttribute("data-index", index);
            listItem.addEventListener("click", function() {
                var dataIndex = this.getAttribute("data-index");
                var place_text = document.getElementById("place_data");
                var data = test_point[dataIndex];
                mostrar_ventana(1);
                showPoint_show(data);
                place_text.innerHTML = `<strong>${data.text}</strong><br>${data.building} - Planta: ${data.floor}`;
                if (data.comment != ""){
                    place_text.innerHTML = place_text.innerHTML + "<br>" + `Comentarios: ${data.comment}`
                }
                // Pasando datos para actualizar punto
                show_data_edit(data)
            });
            puntosLista.appendChild(listItem);
        }
    });
}

function quitarAcentos(texto) {
    return texto.normalize("NFD").replace(/[\u0300-\u036f]/g, "");
}

// *************************************************************
// Muestra información sobre el lugar y el punto en el mapa
// *************************************************************

// Función para mostrar el punto
function showPoint_show(place) {
    show_point.style.left = place.x_percentage + "%";
    show_point.style.top = place.y_percentage + "%";
    show_point.innerHTML = "P." + place.floor
    show_point.style.textAlign = "center";
}

// ****************************************
// Establece los puntos
// mostrar_ventana(2)
// ****************************************
const container_image = document.getElementById("container_image");

// Función para mostrar el punto
function showPoint(pointArg) {
    const point = document.getElementById("point");
    point.style.left = pointArg.x_percentage + "%";
    point.style.top = pointArg.y_percentage + "%";
    var x_percentage = pointArg.x_percentage.toFixed(3);
    var y_percentage = pointArg.y_percentage.toFixed(3);
    coordinates.innerHTML = `{"x_percentage": ${x_percentage}, "y_percentage": ${y_percentage},
     "text": "", "building": "Pabellón A", "floor": "0", "comment": ""},`;
}

// Event listener para detectar clicks en el contenedor de la imagen
container_image.addEventListener("click", function (event) {
    const containerRect = container_image.getBoundingClientRect();
    const containerWidth = containerRect.width;
    const containerHeight = containerRect.height;

    let x = (event.clientX - containerRect.left) / containerWidth * 100;
    let y = (event.clientY - containerRect.top) / containerHeight * 100;

    x = Math.max(0, Math.min(100, x));
    y = Math.max(0, Math.min(100, y));

    showPoint({x_percentage: x, y_percentage: y});
});

// *************************************************************
// Ultimas actualizaciones
// *************************************************************

const updates_button = document.getElementById("last_updates");
updates_button.addEventListener("click", mostrarUpdates);

function mostrarUpdates() {
  const updatesLista = document.getElementById("updates-lista");
  var reversedUpdates = last_updates.slice().reverse();
  updatesLista.innerHTML = ""
  
  reversedUpdates.forEach(function(update){
    var listItem = document.createElement("li");
    listItem.style.fontSize = "50px";
    listItem.innerHTML = update;
    updatesLista.appendChild(listItem)
  })

  mostrar_ventana(3)
}

// *************************************************************
// Introducir nuevo punto
// *************************************************************
const new_point_start = document.getElementById("new_point_proposal");
new_point_start.addEventListener("click", new_point_start_button);

const container_new_image = document.getElementById("container_new_image");
var new_x = 0
var new_y = 0

var button_new = document.getElementById("send_new_point");

function new_point_start_button (){
  mostrar_ventana(4)
}

// Añade un EventListener para el evento "click"
button_new.addEventListener("click", function () {
    const lugar_new = document.getElementById("lugar");
    const edificio_new = document.getElementById("edificio");
    const edificio_text_new = document.getElementById("edificio_text");
    const planta_new = document.getElementById("planta");
    const planta_text_new = document.getElementById("planta_text");
    const observaciones_new = document.getElementById("observaciones");
    var texto = `Nuevo punto:
    {"x_percentage": ${new_x}, "y_percentage": ${new_y}, "text": "${lugar_new.value}", "building": "${edificio_new.value + " - " + edificio_text_new.value}", "floor": "${planta_new.value + " - " + planta_text_new.value}", "comment": "${observaciones_new.value}"},`;
    send_mail(texto)
    mostrar_ventana(0)
}); 


// Función para mostrar el punto
function showPoint_new(pointArg) {
  const new_point_map = document.getElementById("new_point_map");
  new_point_map.style.left = pointArg.x_percentage + "%";
  new_point_map.style.top = pointArg.y_percentage + "%";
}

// Event listener para detectar clicks en el contenedor de la imagen
container_new_image.addEventListener("click", function (event) {
  const containerRect = container_new_image.getBoundingClientRect();
  const containerWidth = containerRect.width;
  const containerHeight = containerRect.height;

  let x = (event.clientX - containerRect.left) / containerWidth * 100;
  let y = (event.clientY - containerRect.top) / containerHeight * 100;

  new_x = Math.max(0, Math.min(100, x)).toFixed(3);
  new_y = Math.max(0, Math.min(100, y)).toFixed(3);

  showPoint_new({x_percentage: new_x, y_percentage: new_y});
});


// *************************************************************
// Editar un punto
// *************************************************************
const edit_point_start = document.getElementById("edit_point_proposal");
edit_point_start.addEventListener("click", edit_point_start_button);

const container_edit_image = document.getElementById("container_edit_image");
var edit_x = 0 // TODO
var edit_y = 0 // TODO

var button_edit = document.getElementById("send_edit_point");

function show_data_edit(data){
  const lugar_edit = document.getElementById("edit_lugar");
  const edificio_edit = document.getElementById("edit_edificio");
  const planta_edit = document.getElementById("edit_planta");
  const observaciones_edit = document.getElementById("edit_observaciones");
  lugar_edit.value = data.text
  edificio_edit.value = data.building
  planta_edit.value = "Planta" + data.floor
  observaciones_edit.value = data.comment
  showPoint_edit(data)
}

function edit_point_start_button (){
  mostrar_ventana(5)
}

// Añade un EventListener para el evento "click"
button_edit.addEventListener("click", function () {
    const lugar_edit = document.getElementById("edit_lugar");
    const edificio_edit = document.getElementById("edit_edificio");
    const planta_edit = document.getElementById("edit_planta");
    const observaciones_edit = document.getElementById("edit_observaciones");
    var texto = `Punto editado:
    {"x_percentage": ${edit_x}, "y_percentage": ${edit_y}, "text": "${lugar_edit.value}", "building": "${edificio_edit.value}", "floor": "${planta_edit.value}", "comment": "${observaciones_edit.value}"},`;
    send_mail(texto)
    mostrar_ventana(0)
}); 


// Función para mostrar el punto
function showPoint_edit(pointArg) {
  const edit_point_map = document.getElementById("edit_point_map");
  edit_point_map.style.left = pointArg.x_percentage + "%";
  edit_point_map.style.top = pointArg.y_percentage + "%";
  edit_x = pointArg.x_percentage
  edit_y = pointArg.y_percentage
}

// Event listener para detectar clicks en el contenedor de la imagen
container_edit_image.addEventListener("click", function (event) {
  const containerRect = container_edit_image.getBoundingClientRect();
  const containerWidth = containerRect.width;
  const containerHeight = containerRect.height;

  let x = (event.clientX - containerRect.left) / containerWidth * 100;
  let y = (event.clientY - containerRect.top) / containerHeight * 100;

  edit_x = Math.max(0, Math.min(100, x)).toFixed(3);
  edit_y = Math.max(0, Math.min(100, y)).toFixed(3);

  showPoint_edit({x_percentage: edit_x, y_percentage: edit_y});
});


// ********************************************
// ENVIAR UN CORREO CON PHP
// ********************************************
function send_mail(message){
  fetch('send_mail.php', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded'
    },
    body: 'mensaje=' + message
  })
  .then(response => {
    if (response.ok) {
      alert('El mensaje ha sido enviado con éxito\nUna vez revisado se añadira la información\nGracias por colaborar');
    } else {
      alert('Lo siento, hubo un problema al enviar el mensaje');
    }
  })
  .catch(error => {
    alert('Lo siento, hubo un problema al enviar el mensaje');
  });
}



