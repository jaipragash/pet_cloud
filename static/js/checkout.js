// Open cart modal
const cart = document.querySelector('#cart');
const cartModalOverlay = document.querySelector('.cart-modal-overlay');

cart.addEventListener('click', () => {
  if (cartModalOverlay.style.transform === 'translateX(-200%)') {
    cartModalOverlay.style.transform = 'translateX(0)';
  } else {
    cartModalOverlay.style.transform = 'translateX(-200%)';
  }
});

// Close cart modal
const closeBtn = document.querySelector('#close-btn');

closeBtn.addEventListener('click', () => {
  cartModalOverlay.style.transform = 'translateX(-200%)';
});

cartModalOverlay.addEventListener('click', (e) => {
  if (e.target.classList.contains('cart-modal-overlay')) {
    cartModalOverlay.style.transform = 'translateX(-200%)';
  }
});

// Add products to cart
const addToCart = document.getElementsByClassName('add-to-cart');
const productRows = document.getElementsByClassName('product-row');

for (let i = 0; i < addToCart.length; i++) {
  const button = addToCart[i];
  button.addEventListener('click', addToCartClicked);
}

function addToCartClicked(event) {
  const button = event.target;
  const cartItem = button.parentElement;
  const price = cartItem.querySelector('.product-price').innerText;
  const imageSrc = cartItem.querySelector('.product-image').src;
  addItemToCart(price, imageSrc);
  updateCartPrice();
}

function addItemToCart(price, imageSrc) {
  const productRow = document.createElement('div');
  productRow.classList.add('product-row');
  const productRows = document.querySelector('.product-rows');
  const cartImages = productRows.querySelectorAll('.cart-image');

  for (let i = 0; i < cartImages.length; i++) {
    if (cartImages[i].src === imageSrc) {
      alert('This item has already been added to the cart');
      return;
    }
  }

  const cartRowItems = `
    <div class="product-row">
      <img class="cart-image" src="${imageSrc}" alt="">
      <span class="cart-price">${price}</span>
      <input class="product-quantity" type="number" value="1">
      <button class="remove-btn">Remove</button>
    </div>
  `;
  productRow.innerHTML = cartRowItems;
  productRows.appendChild(productRow);

  productRow.querySelector('.remove-btn').addEventListener('click', removeItem);
  productRow.querySelector('.product-quantity').addEventListener('change', changeQuantity);
  updateCartPrice();
}

// Remove products from cart
const removeBtn = document.getElementsByClassName('remove-btn');

for (let i = 0; i < removeBtn.length; i++) {
  const button = removeBtn[i];
  button.addEventListener('click', removeItem);
}

function removeItem(event) {
  const btnClicked = event.target;
  btnClicked.parentElement.parentElement.remove();
  updateCartPrice();
}

// Update quantity input
const quantityInputs = document.getElementsByClassName('product-quantity');

for (let i = 0; i < quantityInputs.length; i++) {
  const input = quantityInputs[i];
  input.addEventListener('change', changeQuantity);
}

function changeQuantity(event) {
  const input = event.target;
  if (isNaN(input.value) || input.value <= 0) {
    input.value = 1;
  }
  updateCartPrice();
}

// Update total price
function updateCartPrice() {
  const productRows = document.getElementsByClassName('product-row');
  let total = 0;
  let itemCount = 0;

  for (let i = 0; i < productRows.length; i++) {
    const cartRow = productRows[i];
    const priceElement = cartRow.querySelector('.cart-price');
    const quantityElement = cartRow.querySelector('.product-quantity');
    const price = parseFloat(priceElement.innerText.replace('₹', '').replace('-', '').trim());
    const quantity = quantityElement.value;
    total += price * quantity;
    itemCount += 1;
  }

  document.querySelector('.total-price').innerText = `₹${total}/-`;
  document.querySelector('.cart-quantity').textContent = itemCount;
}

// Purchase items
const purchaseBtn = document.querySelector('.purchase-btn');

purchaseBtn.addEventListener('click', purchaseBtnClicked);

function purchaseBtnClicked() {
  alert('Thank you for your purchase');
  const cartItems = document.querySelector('.product-rows');
  while (cartItems.hasChildNodes()) {
    cartItems.removeChild(cartItems.firstChild);
  }
  updateCartPrice();
}
