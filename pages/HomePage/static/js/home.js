document.querySelectorAll(".add-to-cart").forEach(btn => {
    btn.addEventListener('click', function(e) {
        e.preventDefault(); // Prevent form from submitting the traditional way
        e.stopPropagation();
        let form = this.closest('form'); // Find the closest form ancestor
        let formData = new FormData(form); // Use FormData to grab the form's data

        // Use FormData to get values
        let product_id = formData.get("product_id");
        let product_name = formData.get("product_name");
        let quantity = formData.get("quantity");

        fetch('/add-to-cart', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                product_id: product_id,
                product_name: product_name,
                quantity: quantity
            }),
        })
        .then(response => {
            if(!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            if(data.success){
                alert("Java script Item added to cart successfully");
                // Optionally refresh or redirect the user
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert("There was an error adding the item to the cart.");
        });
    });
});

