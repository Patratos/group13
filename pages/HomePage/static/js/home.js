const add_to_cart_btns = document.querySelectorAll(".add-to-cart")
let items =[];
add_to_cart_btns.forEach((btn) =>{
  btn.addEventListener('click', (e) =>{
    // deny ability to add items to cart if not logged in.
    if (localStorage.getItem("login") === "false" || localStorage.getItem("login") === ""){
      return alert("Please log in to add items to cart")
    }
    const price = e.target.closest('.product-info').children[1].textContent;
    const name = e.target.closest('.product-info').children[0].textContent;
    items.push(
      {
        'name': name,
        'price': price
    }
    )
    localStorage.setItem("items",JSON.stringify(items))
  })
})