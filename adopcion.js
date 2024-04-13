document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('submit_application');
    
    form.addEventListener('submit', function(event) {
        event.preventDefault();
        
        // Inicialización de la validación
        let formIsValid = true;
        const formData = new FormData(form);
        const entries = formData.entries();
        
        for (const [name, value] of entries) {
            const input = form.elements[name];
            if (!value.trim()) {
                // Si algún campo está vacío, marcar el formulario como inválido
                formIsValid = false;
                input.classList.add('error');
                input.nextElementSibling.textContent = 'Este campo es obligatorio.';
            } else {
                input.classList.remove('error');
                input.nextElementSibling.textContent = '';
            }
        }
        
        // Si todos los campos son válidos, mostrar mensaje y enviar formulario
        if (formIsValid) {
            alert('Tu solicitud de adopción ha sido enviada. ¡Gracias por ayudar a un gato a encontrar un hogar amoroso!');
            form.submit(); // Esto enviaría el formulario al servidor
            // Aquí también podrías implementar una función de envío AJAX si no quieres recargar la página.
        } else {
            alert('Por favor, completa todos los campos requeridos.');
        }
    });

    // Añadir un evento listener para cada campo para la validación en tiempo real
    Array.from(form.elements).forEach(element => {
        if (element.type !== 'submit') {
            element.addEventListener('input', function() {
                if (this.value.trim()) {
                    this.classList.remove('error');
                    this.nextElementSibling.textContent = ''; // Asumiendo que hay un elemento para el mensaje de error
                } else {
                    this.classList.add('error');
                    this.nextElementSibling.textContent = 'Este campo es obligatorio.';
                }
            });
        }
    });
});

const form = document.querySelector("form"),
        nextBtn = form.querySelector(".nextBtn"),
        backBtn = form.querySelector(".backBtn"),
        allInput = form.querySelectorAll(".first input");

nextBtn.addEventListener("click", ()=> {
    allInput.forEach(input => {
        if (input.value != "") {
            form.classList.add('secActive');
        } else {
            form.classList.remove('secActive');
        }
    })
})

backBtn.addEventListener("click", ()=> form.classList.remove('secActive'));