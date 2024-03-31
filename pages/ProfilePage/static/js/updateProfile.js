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

    // Saving new values for profile
    let newName = document.getElementById("newName").value
    let newEmail = document.getElementById("newEmail").value
    let newAddress = document.getElementById("newAddress").value
    let newPhone = document.getElementById("newPhone").value

    if (document.getElementById("newName").value.replaceAll(' ', '') === "") {   // if input is empty do nothing
    } else if (newName.length > 30) {                                                    // if input is over 30 chars long, alert.
        return alert("Name too long.")
    }

    if (newEmail === "") {
    } else if (!newEmail.includes("@") || (!newEmail.includes(".com") && !newEmail.includes(".net") && !email.includes(".org"))) {   // if input doesnt include "@" alert.
        return alert("Must be an email")
    }

    if (document.getElementById("newAddress").value === "") {
    } else if (newAddress.length > 30) {           // if input is over 30 chars long, alert.
        alert("Name too long.")
    }

    if (document.getElementById("newPhone").value === "") {
    } else {
        return alert("Must be a phone number")
    }

    fetch('/UpdateProfile', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            username: newName,
            email: newEmail,
            address: newAddress,
            phone: newPhone
        }),
    })
        .then(response => response.json())
        .then(data => {
            if (data.success){
                alert("Profile update successful")
                window.location.href = "/ProfilePage"
            }
            else{
                alert(data.error)
            }
        })
})

const logoutButton = document.querySelector("#logoutBtn")
logoutButton.addEventListener('click', (e) => {
    e.preventDefault()
    window.location.href = "/Logout"
})

