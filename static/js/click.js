const addToCartButtons = document.querySelectorAll('.add-to-cart');

addToCartButtons.forEach((button) => {
  button.addEventListener('click', () => {
    const productId = button.getAttribute('data-product-id');
    const quantity = 1; // You can allow users to specify the quantity

    // Make an AJAX request to add the item to the cart
    fetch('/api/add-to-cart/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ productId, quantity }),
    })
      .then((response) => response.json())
      .then((data) => {
        // Handle the response as needed
        if (data.success) {
          alert('Item added to cart successfully');
        } else {
          alert('Failed to add item to cart');
        }
      })
      .catch((error) => {
        console.error('Error:', error);
      });
  });
});
