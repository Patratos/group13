// deny access to profile if not logged in.
if (localStorage.getItem("login") === "false" || localStorage.getItem("login") === "") {
    window.location.href = "/LoginPage"
}

// showing the current info on the profile
let currentName = localStorage.getItem("username")
let nameHolder = document.getElementById("nameHolder")
let currentEmail = localStorage.getItem("email")
let emailHolder = document.getElementById("emailHolder")
let currentAddress = localStorage.getItem("address")
let addressHolder = document.getElementById("addressHolder")
let currentPhone = localStorage.getItem("phone")
let phoneHolder = document.getElementById("phoneHolder")

nameHolder.innerHTML = '<p id="nameHolder"><strong>Name: </strong>' + currentName + '</p>'
emailHolder.innerHTML = '<p id="emailHolder"><strong>Email: </strong>' + currentEmail + '</p>'
addressHolder.innerHTML = '<p id="addressHolder"><strong>Address: </strong>' + currentAddress + '</p>'
phoneHolder.innerHTML = '<p id="phoneHolder"><strong>Phone: </strong>' + currentPhone + '</p>'

// reset input fields
document.getElementById("newName").value = ""
document.getElementById("newEmail").value = ""
document.getElementById("newAddress").value = ""
document.getElementById("newPhone").value = ""

document.getElementById("newPhone").addEventListener("keypress", function (e) {
    if (e.keyCode < 48 || e.keyCode > 57) { // make sure the user can only input numbers in the phone field.
        e.preventDefault()
    }
})

const updateProfileButton = document.querySelector("#updateProfileBTN")
updateProfileButton.addEventListener('click', (e) => {
    e.preventDefault()
    // saving current and input fields values.
    let currentName = document.getElementById("nameHolder")
    let currentEmail = document.getElementById("emailHolder")
    let currentAddress = document.getElementById("addressHolder")
    let currentPhone = document.getElementById("phoneHolder")

    let newName = document.getElementById("newName").value
    let newEmail = document.getElementById("newEmail").value
    let newAddress = document.getElementById("newAddress").value
    let newPhone = document.getElementById("newPhone").value

    if (newName.replaceAll(' ', '') === "") {   // if input is empty do nothing
    } else if (newName.length > 30) {           // if input is over 30 chars long, alert.
        return alert("Name too long.")
    } else {
        currentName.innerHTML = '<p id="nameHolder"><strong>Name: </strong>' + newName + '</p>'
        localStorage.setItem("username", newName)
    }

    if (document.getElementById("newEmail").value === "") {
    } else if (!newEmail.includes("@") || (!newEmail.includes(".com") && !newEmail.includes(".net") && !email.includes(".org"))) {   // if input doesnt include "@" alert.
        return alert("Must be an email")
    } else {
        currentEmail.innerHTML = '<p id="emailHolder"><strong>Email: </strong>' + newEmail + '</p>'
        localStorage.setItem("email", newEmail)
    }

    if (document.getElementById("newAddress").value === "") {
    } else if (newAddress.length > 30) {           // if input is over 30 chars long, alert.
        alert("Name too long.")
    } else {
        currentAddress.innerHTML = '<p id="addressHolder"><strong>Address: </strong>' + newAddress + '</p>'
        localStorage.setItem("address", newAddress)
    }

    if (document.getElementById("newPhone").value === "") {
    } else if (newPhone.toString().length !== 10) {        // if phone number is not 10 chars long, alert.
        return alert("Must be a phone number")
    } else {
        currentPhone.innerHTML = '<p id="phoneHolder"><strong>Phone: </strong>' + newPhone + '</p>'
        localStorage.setItem("phone", newPhone)
    }

    // reset input fields after submitting correctly
    document.getElementById("newName").value = ""
    document.getElementById("newEmail").value = ""
    document.getElementById("newAddress").value = ""
    document.getElementById("newPhone").value = ""
})

const logoutButton = document.querySelector("#logoutBtn")
logoutButton.addEventListener('click', (e) => {
    e.preventDefault()
    localStorage.setItem("login", "false")
    window.location.href = "/LoginPage"
})
