window.addEventListener("load", function () {
    document.body.style.opacity = 1;
 });

let error = false;
function validateField(input) {

    // If the input is invalid and the error message is not set already
    if (!input.checkValidity() && error === false) {
        // Display the error message once
       // input.reportValidity();
        error = true;

    }
    // When input is valid, clear any custom error message
    else if (input.checkValidity()) {
        input.setCustomValidity('');
        input.style.border = "1px solid rgba(83, 0, 128, 0.891)";
        if(input.id === "password"){
            document.getElementById("psword").style.color = "rgba(83, 0, 128, 0.891);"
        }
        error = false;
    }
}


