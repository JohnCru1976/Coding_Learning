<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $to = "colabora@mapahospital.ovh";
    $subject = "=?UTF-8?B?" . base64_encode("Nueva colaboración") . "?=";

    $headers = "MIME-Version: 1.0" . "\r\n";
    $headers .= "Content-type: text/plain; charset=UTF-8" . "\r\n";

    // Obtiene el mensaje enviado desde JavaScript
    $message = $_POST["mensaje"];

    // Envía el correo
    $success = mail($to, $subject, $message, $headers);

    if ($success) {
        echo "El mensaje ha sido enviado con éxito";
    } else {
        echo "Hubo un problema al enviar el mensaje";
    }
} else {
    echo "Acceso no autorizado";
}
?>