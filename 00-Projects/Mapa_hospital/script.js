const container_image = document.getElementById("container_image");
const point = document.getElementById("point");
const coordinates = document.getElementById("coordinates");
const pointButton = document.getElementById("pointButton");
const testPointContent = document.getElementById("testPointContent");

// Función para mostrar el punto
function showPoint(pointArg) {
    point.style.left = pointArg.x_percentage + "%";
    point.style.top = pointArg.y_percentage + "%";
    coordinates.value = `X: ${pointArg.x_percentage.toFixed(3)}%, Y: ${pointArg.y_percentage.toFixed(3)}%`;
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

    showPoint({ ...test_point, x_percentage: x, y_percentage: y });
});

// Event listener para el botón "Point"
pointButton.addEventListener("click", function () {
    showPoint(test_point);
    showTestPointContent(test_point);
});

// Función para mostrar el contenido de test_point
function showTestPointContent(pointArg) {
    const content = `ID: ${pointArg.id}, X: ${pointArg.x_percentage}%, Y: ${pointArg.y_percentage}%, Text: ${pointArg.text}, Building: ${pointArg.building}, Floor: ${pointArg.floor}`;
    testPointContent.textContent = content;
}