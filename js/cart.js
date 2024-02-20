// deny access to cart if not logged in.
if (localStorage.getItem("login") === "false" || localStorage.getItem("login") === ""){
  window.location = "LoginPage.html"
}

const cartTable = document.querySelector('.cart-table')
window.addEventListener('load', (e) => {
    let items = JSON.parse(localStorage.getItem("items"));
    items.forEach((item) => {
        const newRow = cartTable.insertRow(1);
        newRow.classList.add("cart-item");
        const item_name = newRow.insertCell(0);
        item_name.classList.add("item-name");
        item_name.textContent = item.name;
        const itemQuantity = newRow.insertCell(1);
        itemQuantity.innerHTML = `<input type="number" value="1" min="1" class="item-quantity">`;
        itemQuantity.addEventListener('input', calcTotal);
        itemQuantity.addEventListener('change', calcTotal);
        const itemPrice = newRow.insertCell(2);
        itemPrice.classList.add('item-price');
        itemPrice.textContent = item.price;
        // const itemTotal = newRow.insertCell(3);
        // itemTotal.classList.add('item-total');
        const removeBTNtd = newRow.insertCell(3);
        removeBTNtd.innerHTML = `<button class="remove-item">Remove</button>`;

        const removeButton = removeBTNtd.querySelector('button');
        removeButton.addEventListener('click', () => {
            newRow.remove();
            calcTotal();
        })
        calcTotal();
    })
})

const calcTotal = () => {
    let totalPrice = 0;
    const rows = document.querySelectorAll('tr.cart-item');
    rows.forEach((item) => {
        const quantity = parseInt(item.cells[1].children[0].value);
        const price = parseFloat(item.cells[2].textContent);
        totalPrice += price * quantity;
    })
    totalPrice = totalPrice.toFixed(2);
    const total = document.querySelector('span.total-value');
    total.textContent = `$ ${totalPrice}`;
}