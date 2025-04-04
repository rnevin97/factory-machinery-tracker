// Declared variables
var companyEmail; 
var companyName;
var firstName;
var lastName;
var password;
var confirmPassword;
var phoneNumber;
var jobTitle;
var regForm;

/**
 * Initializing variables: Assign form elements
 */ 
function initialisePage(){
    this.firstName = document.getElementById("first-name");
    this.lastName=document.getElementById("last-name");
    this.phoneNumber=document.getElementById("phonenumber");
    this.companyName = document.getElementById("cmp-name");
    this.companyEmail = document.getElementById("cmp-email");
    this.password=document.getElementById("password");
    this.confirmPassword=document.getElementById("confirm-password");
    this.jobTitle = document.getElementById("jobtitle");
    this.regForm = document.getElementById("regForm");

    this.setPlaceholders();
}

/**
 *  function for setting placeholders in the input fields for registration form
 */
function setPlaceholders() {
    this.firstName.placeholder = "First Name";
    this.lastName.placeholder = "Last Name";
    this.phoneNumber.placeholder = "Phone Number";
    this.companyEmail.placeholder = "Company Email";
    this.companyName.placeholder = "Company Name";
    this.password.placeholder = "Password";
    this.confirmPassword.placeholder = "Confirm Password";
    this.jobTitle.placeholder = "Job Title";
}


function validateForm() {
    var isValid = true;
        // get all required fields
    var requiredFields = document.querySelectorAll("#reg-form input[required=true]");
    for(i=0; i< requiredFields.length; i++){ //loop for checking if required input fields are filled or not
        if(requiredFields[i].value == "") {
            requiredFields[i].nextElementSibling.textContent = "This is Required Field."; //if input fields are not filled, this error message will pop up
            isValid = false;
        } else {
            requiredFields[i].nextElementSibling.textContent = "";
            if (this.companyEmail.value==""|| !this.companyEmail.value.includes("@") || !this.companyEmail.value.includes(".")){
                this.companyEmail.nextElementSibling.textContent="Please enter a valid email address.";
                isValid= false;
            }

            if (this.phoneNumber.value==/^\d{10}$/){
                    this.phoneNumber.nextElementSibling.textContent="Please enter 10 digit phone number.";
            }
            if (this.password.value.length<6){ //password must be at least 6 alpha-numeric/digit
                this.password.nextElementSibling.textContent="Password must be at least 6 digit.";
                isValid= false;
            }

            if(this.password.value != this.confirmPassword.value) {   //validation for password and confirm password
                    this.confirmPassword.nextElementSibling.textContent="Passwords do not match.";
                isValid= false;
            }

            //Getting registered users in an array to check if email is already registerd
            var users = JSON.parse(sessionStorage.getItem("RegisterdUsers"));
            var isUserPresent = users.filter(user => user[1].companyEmail === this.companyEmail.value );
            // if length is greater than 0 means email is already registerd, so show alert message
            if(isUserPresent.length > 0) {
                this.companyEmail.nextElementSibling.textContent="Email already registerd";
                isValid = false;
        
            }
        }
    }
    return isValid;
}

/**
 * 
 * This function is called when focusOut on required fields to check if is has value or not
 */
function checkIfRequired(id) {
    var element = document.getElementById(id);
    if(element.value == "") {
        element.nextElementSibling.textContent = "This is Required Field";
    } else {
        element.nextElementSibling.textContent = "";
    }
}


function registerForm(e) {
    e.preventDefault();  //prevent default behavior of submit action to prevent page reload
    if(this.validateForm()){
        this.saveRegisterationDetailInSession();
        // Show alert after successful registeration
        var alertBox = document.getElementsByClassName("alertBox");
        alertBox[0].classList.remove("hide");
        alertBox[0].getElementsByTagName("p")[0].textContent = "Verification email has been sent to your email address. Use link in email to complete registeration"
    }
}   


/**
 * Store form data in session
 */
function saveRegisterationDetailInSession() {  
    var tempArray;   
    //Getting registered users in an array
    var users = JSON.parse(sessionStorage.getItem("RegisterdUsers"));
    var user = {
        "firstName" : this.firstName.value,
        "lastName" : this.lastName.value,
        "phoneNumber" : this.phoneNumber.value,
        "companyName" : this.companyName.value,
        "companyEmail" : this.companyEmail.value,
        "password" : this.password.value,
        "jobTitle" : this.jobTitle.value
    };

    var userMap = new Map; //using Map key value pairs to store user data
    userMap.set(Date.now(),user); //Date.now() will help to give unique identity to users
    
    if(users) {
        // add new user to session.
        // if there are existing registered users in session, add new user to existing array
        tempArray = users.concat(Array.from(userMap))
    
    } else {
        // if no existing registerd users present, add simply user to array
        tempArray = Array.from(userMap)
    }
 

    sessionStorage.setItem("RegisterdUsers" , JSON.stringify(tempArray));
}



