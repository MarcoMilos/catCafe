$(document).ready(function() {
    $('#loginForm').on('submit', function(e) {
        e.preventDefault(); // Prevent the default form submission

        var username = $('input[name="uname"]').val(); // Get username from form input
        var password = $('input[name="psw"]').val(); // Get password from form input

        $.ajax({
            url: 'https://plpcollado.pythonanywhere.com/login', // Target URL for the login request
            method: 'POST', // Method type
            contentType: "application/x-www-form-urlencoded; charset=UTF-8", // Ensure proper header for POST
            data: {
                username: username,
                password: password
            },
            success: function(response) {
                if (response.error) {
                    alert(response.error); // Display error message if login fails
                } else {
                    if (response.admin) {
                        window.location.href = '/opcionCafe-Admin.html'; // Redirect admin to admin page
                    } else {
                        window.location.href = '/productos-Usuario.html'; // Redirect regular user to user page
                    }
                }
            },
            error: function(xhr) {
                // Handle errors
                alert('Error logging in. Please try again. Status: ' + xhr.status);
            }
        });
    });
});



