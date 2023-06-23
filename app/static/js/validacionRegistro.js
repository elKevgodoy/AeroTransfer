$().ready(function() {
    $("#idFormRegistroTransfer").validate({
        rules: {
            id_first_name: {
                required: true,
                minlength: 3
            },
            id_last_name: {
                required: true,
                minlength: 3
            },
            inputLicencia: {
                required: true,
                minlength: 8
            },
            inputPatente: {
                required: true,
                minlength: 5
            },
            inputAsientos: {
                required: true,
                minlength: 1
            },
            inputVehiculo: {
                required: true,
                minlength: 4
            },
            id_username: {
                required: true,
                minlength: 3
            },
            id_password1: {
                required: true,
                minlength: 6
            },
            id_password2: {
                required: true,
                equalTo: "#id_password1"
            },
        },
        messages: {
            id_first_name: {
                required: "Debes de ingresar un nombre",
                minlength: "La calle debe tener al menos 3 caracteres"
            },
            id_last_name: {
                required: "Debes ingresar un apellido",
                minlength: "Tu Apellido debe tener al menos 3 caracteres"
            },
            inputLicencia: {
                required: "Debes ingresar tu numero de licencia",
                minlength: "La licencia debe tener al menos 8 caracteres"
            },
            inputPatente: {
                required: "Debes ingresar tu patente",
                minlength: "La patente debe tener al menos 5 caracteres"
            },
            inputAsientos: {
                required: "Debes ingresar la cantidad de asientos",
                minlength: "El minimo de asientos es 1"
            },
            inputVehiculo: {
                required: "Debes ingresar tu tipo de vehiculo",
                minlength: "Como minimo puedes usar un Auto"
            },
            id_username: {
                required: "Debes ingresar un Username",
                minlength: "El username debe tener al menos 3 caracteres"
            },
            id_password1: {
                required: "Debes ingresar la contraseña",
                minlength: "La contraseña debe tener al menos 6 caracteres"
            },
            id_password2: {
                required: "Debes repetir la contraseña",
                equalTo: "Las contraseñas no coinciden"
            }
        }

    });
});