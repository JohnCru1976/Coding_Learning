const test_image = document.getElementById("test_image")
const show_image = document.getElementById("show_image")
const list_places = document.getElementById("list_places")

const container_image = document.getElementById("container_image");
const container_show_image = document.getElementById("container_show_image");

const point = document.getElementById("point");
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
    if (num == 0) {
      list_places.style.display = "block"; 
      show_image.style.display = "none";
      test_image.style.display = "none";
    }
    if (num == 1) {
        list_places.style.display = "none"; 
        show_image.style.display = "block";
        test_image.style.display = "none";
      }
      if (num == 2) {
        list_places.style.display = "none"; 
        show_image.style.display = "none";
        test_image.style.display = "block";
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
// Función para mostrar el punto
function showPoint(pointArg) {
    point.style.left = pointArg.x_percentage + "%";
    point.style.top = pointArg.y_percentage + "%";
    var x_percentage = pointArg.x_percentage.toFixed(3);
    var y_percentage = pointArg.y_percentage.toFixed(3);
    coordinates.innerHTML = `{"x_percentage": ${x_percentage}, "y_percentage": ${y_percentage},
     "text": "", "building": "Pabellón A", "floor": "0", "comment": ""},`;
}

// Event listener para detectar clics en el contenedor de la imagen
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




