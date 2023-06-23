$().ready(function() {
    $("#idFormReserva").validate({
        rules: {
            inputCalle: {
                required: true,
                minlength: 3
            },
            inputNumero: {
                required: true,
                minlength: 4

            },
            inputCiudad: {
                required: true,
                minlength: 3
            },
            inputPasajeros: {
                required: true,
                maxlength: 2
            }
        },
        messages: {
            inputCalle: {
                required: "Debes de ingresar una calle",
                minlength: "La calle debe tener al menos 3 caracteres"
            },
            inputNumero: {
                required: "Debes ingresar el numero de calle",
                minlength: "El numero tiene como minimo 4 caracteres"
            },
            inputCiudad: {
                required: "Debes ingresar la ciudad",
                minlength: "La ciudad debe tener al menos 3 caracteres"
            },
            inputPasajeros: {
                required: "Debes ingresar la cantidad de pasajeros",
                maxlength: "Ingresa una cantidad valida"
            }
        }

    });
});
