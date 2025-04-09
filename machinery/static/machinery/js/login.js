function initialisePage() {

    document.getElementById("loginForm").addEventListener("submit", async function(e) {
        
        e.preventDefault();
    
        const formData = new FormData(this);
        const username = formData.get("username");
        const password = formData.get("password");
    
        const loginRes = await fetch("/api/login/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ username, password })
        });
        
       
        if (loginRes.ok) {
            await loginRes.json().then((res)=>{
                console.log(res)
                window.location.href = res.redirect_url;
            })
        } else {
            alert("Login failed");
        }
    });

}


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

