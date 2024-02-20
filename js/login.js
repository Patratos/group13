// reset input fields
document.getElementById("username").value = ""
document.getElementById("password").value = ""

const loginButton = document.querySelector("#loginBtn")
loginButton.addEventListener('click', (e) =>{
  e.preventDefault()
  const username = document.getElementById("username").value
  const storedName = localStorage.getItem("username")
  const password = document.getElementById("password").value
  const storedPassword = localStorage.getItem("password")

  if(username !== storedName || password !== storedPassword) {
      alert('Wrong credentials')
  }else {
      localStorage.setItem("login", "true")
      alert("Login Successful")
      // go to profile page after successful login.
      window.location = "HomePage.html"
  }
})
