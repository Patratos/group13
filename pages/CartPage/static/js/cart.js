window.addEventListener('load', () => {
    // Load cart items from localStorage (if needed) and initialize the table
    let items = JSON.parse(localStorage.getItem("items")) || [];
    const cartTable = document.querySelector('.cart-table');

    items.forEach((item) => {
        const newRow = cartTable.insertRow();
        newRow.classList.add("cart-item");
        newRow.setAttribute('data-id', item.id); // Make sure each item has a unique identifier

        const cellImage = newRow.insertCell(0);
        cellImage.innerHTML = `< img src="/static/media/products_img/${item.image_path}" style="width:100px; height:100px; object-fit: cover;">`;

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
        cellRemove.querySelector('.remove-item').addEventListener('click', function () {
            newRow.remove();
            updateLocalStorageOnRemove(item.id);
            calcTotal();
        });
    });

    calcTotal(); // Initial total calculation

    // Listen for clicks on the Update Cart button
    document.querySelector('.update-cart').addEventListener('click', function () {
        updateCart();
    });
});

// Function to recalculate the total cost of the cart
function updateCart() {
    let items = [];
    // Collect data from each row in the table
    document.querySelectorAll('.cartArea table tbody tr').forEach(row => {
        const productName = row.cells[1].textContent.trim();  // Gets the product name from the second cell
        const quantity = parseInt(row.querySelector('input[type="number"]').value); // Gets the quantity from the input
        items.push({"Product-name": productName, "Quantity": quantity});
    });

    console.log("Updating cart with items:", items);  // Log the items array to the console for verification

    fetch('/CartPage', {  // Make sure this matches the Flask route for updating the cart
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({items: items})
    })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                // alert('Cart updated successfully.');
                location.reload();  // Reload to reflect the updated data
            } else {
                // alert('Failed to update cart: ' + data.messages.join('\n'));
            }
        })
        .catch(error => {
            console.error('Error updating cart:', error);
            // alert('Error updating cart: ' + error.message);
        });
}

document.querySelector('.update-cart').addEventListener('click', updateCart);  // Attach the updateCart function to the update button

// Function to recalculate the total cost of the cart
function calcTotal() {
    let totalPrice = 0;
    document.querySelectorAll('.cartArea table tbody tr').forEach(row => {
        const price = parseFloat(row.cells[2].textContent.replace('$', '').trim());
        const quantity = parseInt(row.querySelector('input[type="number"]').value);
        const total = price * quantity;
        row.cells[4].textContent = `$${total.toFixed(2)}`;  // Update the Total cell
        totalPrice += total;
        updateGrandTotal();
    });
    document.querySelector('.total-value').textContent = `$${totalPrice.toFixed(2)}`;  // Update the total display
}


document.querySelectorAll('.remove-item').forEach(button => {
    button.addEventListener('click', function () {
        const row = button.closest('.cart-item');
        const productName = row.querySelector('.item-name').textContent.trim();
        fetch('/CartPage/remove', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({"Product-name": productName})
        })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    // alert('Item removed successfully.');
                    row.remove();  // Remove the row from the table
                    calcTotal();  // Recalculate the total if needed
                } else {
                    // alert('Failed to remove item: ' + data.message);
                }
            })
            .catch(error => {
                console.error('Error removing item:', error);
                // alert('Error removing item: ' + error.message);
            });
    });
});


// Function to update localStorage after an item is removed
function updateLocalStorageOnRemove(itemId) {
    let items = JSON.parse(localStorage.getItem("items")) || [];
    items = items.filter(item => item.id !== itemId);
    localStorage.setItem("items", JSON.stringify(items));
}

// Attach event listeners to each "Remove" button
document.querySelectorAll('.remove-item').forEach(button => {
    button.addEventListener('click', function () {
        const row = this.closest('tr');
        const productName = row.querySelector('td:nth-child(2)').textContent.trim();  // Assuming the product name is in the second cell

        fetch('/CartPage/remove', {  // Ensure this URL is correct according to your Flask routes
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({"Product-name": productName})
        })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    // alert('Item removed successfully.');
                    row.remove();  // Remove the row from the DOM
                    calcTotal();  // Recalculate total if necessary
                } else {
                    // alert('Failed to remove item: ' + data.message);
                }
            })
            .catch(error => {
                console.error('Error removing item:', error);
                // alert('Error removing item: ' + error.message);
            });
    });
});
function updateGrandTotal() {
    let grandTotal = 0;
    document.querySelectorAll('.cartArea table tbody tr').forEach(row => {
        const total = parseFloat(row.cells[4].textContent.replace('$', '').trim());
        grandTotal += total;
    });
    document.querySelector('#grandTotal').textContent = `$${grandTotal.toFixed(2)}`;
}