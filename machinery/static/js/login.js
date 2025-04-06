window.addEventListener("load", function () {
    document.body.style.opacity = 1;
 });


/**
 * 
 * This function is called when focusOut on required fields to check if is has value or not
 */
function checkField(id) {
    var element = document.getElementById(id);
    if(element.value == "") {
        element.nextElementSibling.textContent = "This is Required Field"; // setting warning message
    } else {
        element.nextElementSibling.textContent = ""; //if field is not empty, there will be on warning message, set content to empty string
    }
}

