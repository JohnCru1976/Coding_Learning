// Escuchar mensajes provenientes de los frames
window.addEventListener("message", function(event) {
    let frame = document.getElementById("web");
    frame.src = event.data;
});


