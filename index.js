$(document).ready(function() {
    // Handle the form submission
    $('body').on('click', 'button[type="submit"]', function(e) {
        e.preventDefault();

        // Get the username and password from the form
        var username = $('input[name="uname"]').val();
        var password = $('input[name="psw"]').val();

        // Send the username and password to the server
        $.ajax({
            url: '/checkUser',  // The endpoint on your Flask server
            method: 'POST',
            data: {
                username: username,
                password: password
            },
            success: function(response) {
                // If the user is an admin, redirect to the admin page
                if (response.admin) {
                    window.location.href = '/opcioCafe-Admin-html';
                }
                // If the user is not an admin, redirect to the user page
                else {
                    window.location.href = '/opcioCafe-Usuario-html';
                }
            },
            error: function() {
                // Handle any errors
                alert('Error logging in. Please try again.');
            }
        });
    });
});