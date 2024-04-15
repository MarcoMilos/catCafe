$(document).ready(function() {
    $('#registrationForm').submit(function(event) {
        event.preventDefault(); // Evitar el envío del formulario por defecto

        // Obtener los valores del formulario
        var username = $('input[name="uname"]').val();
        var password = $('input[name="psw"]').val();

        // Verificar que los campos no estén vacíos
        if (username.trim() === '' || password.trim() === '') {
            alert("Por favor, completa todos los campos.");
            return;
        }

        // Enviar la solicitud POST al endpoint de registro
        $.ajax({
            type: 'POST',
            url: 'https://plpcollado.pythonanywhere.com//register', // Ruta del endpoint de registro en el servidor
            data: {
                username: username,
                password: password
            },
            success: function(response) {
                // Manejar la respuesta del servidor
                if (response.success) {
                    alert("Registro exitoso. ¡Bienvenido a Miaw Cat Cafe!");
                    // Redireccionar al usuario a la página de inicio de sesión
                    window.location.href = "/index.html";
                } else {
                    alert("Error: " + response.error);
                }
            },
            error: function(xhr, status, error) {
                // Manejar errores de la solicitud
                console.error("Error en la solicitud:", status, error);
                alert("Error de conexión. Inténtalo de nuevo más tarde.");
            }
        });
    });
});