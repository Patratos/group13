// reset input fields
document.getElementById("userName").value = ""
document.getElementById("email").value = ""
document.getElementById("psw").value = ""
document.getElementById("pswRepeat").value = ""

const registerButton = document.querySelector("#registerBtn")
registerButton.addEventListener('click', (e) => {
    e.preventDefault()
    let username = document.getElementById("userName").value
    let email = document.getElementById("email").value
    let password = document.getElementById("psw").value
    let re_password = document.getElementById("pswRepeat").value

    // Validate Fields
    if (username.replaceAll(' ', '') === "") {
        return alert("Enter username")
    } else if (username.length > 30) {
        return alert("Name too long")
    } else if (!email.includes("@") || (!email.includes(".com") && !email.includes(".net") && !email.includes(".org"))) {
        return alert("Must be an email")
    } else if (password.length < 5) {
        alert("Password too short")
    } else if (password !== re_password) {
        alert("Passwords doesn't match")
    } else {
        // Create JSON and send to server
        const registerData = {
            username: username,
            email: email,
            address: "",
            phone: "",
            password: password
        }

        fetch('/RegisterPage', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(registerData)
        })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    alert("Registered Successfully")
                    window.location.href = "/LoginPage"
                } else {
                    alert("Registration failed")
                }
            })
    }
})
