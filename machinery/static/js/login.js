var password; //defining variables
var email;
var emailErr;


/**
 * Initializing variables: Assign form elements
 */ 
function initialisePage(){
  
    this.password=document.getElementById("password");
    this.emailErr=document.getElementsByClassName("warningMessage email");
    this.email=document.getElementById("email");
    this.setPlaceholders();
}

/**
 * Set Placeholders for Form Inputs
 */
function setPlaceholders() { 
   
    this.password.placeholder = "Password";
    this.email.placeholder = "Email";
 
}

/**
 * 
 * This function is called when focusOut on required fields to check if is has value or not
 */
function checkIfRequired(id) {
    var element = document.getElementById(id);
    if(element.value == "") {
        element.nextElementSibling.textContent = "This is Required Field"; // setting warning message
    } else {
        element.nextElementSibling.textContent = ""; //if field is not empty, there will be on warning message, set content to empty string
    }
}

function submitForm(e) {
    e.preventDefault();  //prevent default behavior of submit action to prevent page reload
    let isValid=true;

    if (this.email.value==""|| !this.email.value.includes("@") || !this.email.value.includes(".")){ //validation on email field
        emailErr[0].textContent="Please enter a valid email address.";
        isValid= false;
    }
    
    // If its a valid form proceed with form submission
    if(isValid) {
        //Getting registered users in an array
        var users = JSON.parse(sessionStorage.getItem("RegisterdUsers")); 
        if(users) {
             // if we have registered users, then filter array and get user whose email & password match with form input 
            var isValidUser = users.filter(user => user[1].companyEmail === this.email.value && user[1].password === this.password.value);
            // if length is greater than 0 means user exist in register users array
            if(isValidUser.length > 0) {
                // store user details in session and redirect to dashboard
                sessionStorage.setItem("loggedInUser" , JSON.stringify(isValidUser));
                window.location.href = "./dashboard.html";
            } 
        }

        // alert box to show if an unregistered user tries to log in
        var alertBox = document.getElementsByClassName("alertBox"); 
        alertBox[0].classList.remove("hide");
        alertBox[0].getElementsByTagName("p")[0].textContent = "Incorrect Username or Password"
        
    }
    
}   
