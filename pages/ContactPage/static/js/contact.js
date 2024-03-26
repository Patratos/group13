// reset input fields
username = document.getElementById("contactName").value = ""
email = document.getElementById("contactEmail").value = ""
subject = document.getElementById("contactSubject").value = ""
content = document.getElementById("contactContent").value = ""

const contactButton = document.querySelector("#contactBtn")
contactButton.addEventListener('click', (e) =>{
  e.preventDefault()
  let username = document.getElementById("contactName").value
  let email = document.getElementById("contactEmail").value
  let subject = document.getElementById("contactSubject").value
  let content = document.getElementById("contactContent").value

  if (username.replaceAll(' ', '') === ""){
    return alert("Enter username")
  } else if (!email.includes("@") || (!email.includes(".com") && !email.includes(".net") && !email.includes(".org"))){
    return alert("Must be an email")
  } else {
      username = ""
      email = ""
      subject = ""
      content = ""
      alert("Thank you, we will contact you soon.")
  }
})