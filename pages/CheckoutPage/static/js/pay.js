document.getElementById("creditCard").value = ""
document.getElementById("expiryDate").value = ""
document.getElementById("cvv").value = ""

document.getElementById("creditCard").addEventListener("keypress", function (event){
    if (event.keyCode < 48 || event.keyCode > 57) { // make sure the user can only input numbers in the phone field.
      event.preventDefault()
    }
  })
document.getElementById("expiryDate").addEventListener("keypress", function (e){
    if (e.key !== "/") { // make sure the user can only input numbers in the phone field.
      if (e.keyCode < 48 || e.keyCode > 57){
        e.preventDefault()
      }
    }
  })
// document.getElementById("expiryDate").addEventListener("keypress", function (e){
//     if ((e.keyCode < 48 || e.keyCode > 57) || e.key !== "/") { // make sure the user can only input numbers in the phone field.
//       e.preventDefault()
//     }
//   })
document.getElementById("cvv").addEventListener("keypress", function (event){
    if (event.keyCode < 48 || event.keyCode > 57) { // make sure the user can only input numbers in the phone field.
      event.preventDefault()
    }
  })

const payment = document.querySelector("#payBtn")
payment.addEventListener('click', (e)=>{
  e.preventDefault()

  let creditCard = document.getElementById("creditCard").value
  let expiryDate = document.getElementById("expiryDate").value
  let cvv = document.getElementById("cvv").value


  if (creditCard.length !== 16){
    return alert("Credit Card Number Not Valid")
  } else if (!expiryDate.includes("/")){
    return alert("Expiry Date Not Valid")
  } else if (cvv.length !== 3){
    return alert("CVV Not Valid")
  } else {
    alert("Thank you!")
    localStorage.removeItem("items")
    window.location = "CartPage.html"
  }
})
