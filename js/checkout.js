checkoutButton = document.querySelector("#checkoutBtn")
checkoutButton.addEventListener('click', (e)=>{
  if (localStorage.getItem("address") === "" || localStorage.getItem("phone") === ""){
      return alert("Please add an address and/or phone number to continue")
  } else {
    window.location = "CheckoutPage.html"
  }
})
