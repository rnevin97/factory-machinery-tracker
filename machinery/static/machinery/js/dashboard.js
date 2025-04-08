function loadUserData() {

    var users = JSON.parse(sessionStorage.getItem("RegisterdUsers"));
    document.querySelector("#reg-table tbody").innerHTML = users.map(user => `<tr><td>${JSON.stringify(user[0])}</td><td>${JSON.stringify(user[1])}</td></tr>`).join('')

    var loggedUser = JSON.parse(sessionStorage.getItem("loggedInUser"));
    document.querySelector("#logged-table tbody").innerHTML = loggedUser.map(user => `<tr><td>${JSON.stringify(user[0])}</td>       <td>${JSON.stringify(user[1])}</td></tr>`).join('')

}