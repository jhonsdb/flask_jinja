const email = document.getElementById('correo');
const password = document.getElementById('contraseña');
const login = document.getElementById('login');

    // Función para validar el formulario
    function validar() {
        if (email.value === "" || password.value === "") {
            alert("Debe llenar todos los campos");
            return false;
        } else {
            return true;
        }
    }

    // Función para manejar el envío del formulario
    function handleSubmit(event) {
        event.preventDefault(); // Evita que el formulario se envíe normalmente

        if (validar()) {
            // Almacenar los valores en el almacenamiento local
            localStorage.setItem('correo', email.value);
            localStorage.setItem('contraseña', password.value);

            // Puedes redirigir a otra página o realizar otras acciones aquí
            console.log("Formulario enviado correctamente");
        }
    }

    // Agregar el evento de envío al formulario
    login.addEventListener('submit', handleSubmit);