const email = document.getElementById('correo');
const password = document.getElementById('contraseña');

function validar() {
    if (email.value == "" || password.value == "") {
        alert("Debe llenar todos los campos");
        return false;
    } else {
        return true;
    }
}