<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $nombre = $_POST["nombre"];
    $correo = $_POST["correo"];
    $mensaje = $_POST["mensaje"];
    
    $destinatario = "colabora@mapahospital.ovh"; // Reemplaza con la dirección de correo de destino
    $asunto = "Nuevo mensaje de $nombre";

    $cabeceras = "From: $correo\r\n";
    $cabeceras .= "Reply-To: $correo\r\n";
    
    if (mail($destinatario, $asunto, $mensaje, $cabeceras)) {
        echo "El correo ha sido enviado con éxito.";
    } else {
        echo "Hubo un error al enviar el correo.";
    }
}
?>