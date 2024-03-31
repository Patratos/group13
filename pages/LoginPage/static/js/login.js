// reset input fields
document.getElementById("email").value = ""
document.getElementById("password").value = ""

const loginButton = document.querySelector("#loginBtn")
loginButton.addEventListener('click', (e) => {
    e.preventDefault()
    const email = document.getElementById("email").value
    const password = document.getElementById("password").value

    fetch('/LoginPage', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            email: email,
            password: password
        }),
    })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert("Logged in Successfully")
                window.location.href = "/HomePage"
            } else {
                alert(data.error)
            }
        })
})
