function initialisePage() {

    document.getElementById("regForm").addEventListener("submit", async function(e) {

        e.preventDefault();
    
        const formData = new FormData(this);
        const username = formData.get("userName");
        const password = formData.get("password");
        const role = formData.get("role");
        const email = formData.get("email");
        const firstName = formData.get("firstName");
        const lastName = formData.get("lastName");
        const companyName = formData.get("companyName");
    
        const registerRes = await fetch("/api/register/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ username, password, role, email, firstName, lastName, companyName })
        });
        
       
        if (registerRes.ok) {
            await registerRes.json().then((res)=>{
                console.log(res)
                window.location.href = res.redirect_url;
            })
        } else {
            alert("Registration failed");
        }
    });

}

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
        
        if (input.id === "password" && input.checkValidity()) {
            input.addEventListener("focusout", function() {
                // Apply color to the password field when it loses focus
                document.getElementById("psword").style.setProperty("color", "rgba(83, 0, 128, 0.891)", "important");
            });
        }
        
        if (input.id === "job") {
            // Change color to black when the job input loses focus
            input.addEventListener("focusout", function() {
                this.style.setProperty("color", "black", "important");
            });
            error = false;
        }
    }

}





