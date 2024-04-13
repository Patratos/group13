window.addEventListener('load', () => {
    // Load cart items from localStorage (if needed) and initialize the table
    let items = JSON.parse(localStorage.getItem("items")) || [];
    const cartTable = document.querySelector('.cart-table');

    items.forEach((item) => {
        const newRow = cartTable.insertRow();
        newRow.classList.add("cart-item");
        newRow.setAttribute('data-id', item.id); // Make sure each item has a unique identifier

        const cellImage = newRow.insertCell(0);
        cellImage.innerHTML = `<img src="/static/media/products_img/${item.image_path}" style="width:100px; height:100px; object-fit: cover;">`;

        const cellName = newRow.insertCell(1);
        cellName.textContent = item.name;

        const cellPrice = newRow.insertCell(2);
        cellPrice.classList.add('item-price');
        cellPrice.textContent = item.price;

        const cellQuantity = newRow.insertCell(3);
        cellQuantity.innerHTML = `<input type="number" class="item-quantity" value="${item.quantity}" min="1" style="width: 50px;">`;
        cellQuantity.querySelector('.item-quantity').addEventListener('input', calcTotal);

        const cellTotal = newRow.insertCell(4);
        cellTotal.classList.add('item-total');
        cellTotal.textContent = (item.price * item.quantity).toFixed(2);

        const cellRemove = newRow.insertCell(5);
        cellRemove.innerHTML = `<button class="remove-item">Remove</button>`;
        cellRemove.querySelector('.remove-item').addEventListener('click', function() {
            newRow.remove();
            updateLocalStorageOnRemove(item.id);
            calcTotal();
        });
    });

    calcTotal(); // Initial total calculation

    // Listen for clicks on the Update Cart button
    document.querySelector('.update-cart').addEventListener('click', function() {
        updateCart();
    });
});

// Function to recalculate the total cost of the cart
function calcTotal() {
    let totalPrice = 0;
    document.querySelectorAll('.cart-item').forEach(row => {
        const price = parseFloat(row.cells[2].textContent);
        const quantity = parseInt(row.querySelector('.item-quantity').value);
        const total = price * quantity;
        row.cells[4].textContent = total.toFixed(2); // Update the total cell
        totalPrice += total;
    });
    document.querySelector('.total-value').textContent = `$${totalPrice.toFixed(2)}`;
}

// Function to update the cart on the server
function updateCart() {
    let items = [];
    document.querySelectorAll('.cart-item').forEach(row => {
        const id = row.getAttribute('data-id');
        const quantity = parseInt(row.querySelector('.item-quantity').value);
        items.push({id: id, quantity: quantity});
    });

    fetch('/CartPage', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({items: items})
    })
    .then(response => response.json())
    .then(data => {
        if(data.success) {
            alert(data.message);
            location.reload(); // Optionally reload to fetch and display updated data
        } else {
            alert('Failed to update cart');
        }
    })
    .catch(error => {
        console.error('Error updating cart:', error);
    });
}

// Function to update localStorage after an item is removed
function updateLocalStorageOnRemove(itemId) {
    let items = JSON.parse(localStorage.getItem("items")) || [];
    items = items.filter(item => item.id !== itemId);
    localStorage.setItem("items", JSON.stringify(items));
}
