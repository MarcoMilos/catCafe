
function loadCart() {
    let cart = JSON.parse(localStorage.getItem('cart')) || [];
    
    cart.forEach(product => {
      // Añadir cada producto al DOM del carrito
      // Tendrás que crear HTML y agregarlo al DOM de tu página de carrito
      // Esto es solo un ejemplo, necesitarás ajustarlo a tu estructura HTML y estilos
      const productElement = document.createElement('div');
      productElement.innerHTML = `
        <div class="product" data-id="${product.id}">
          <img src="${product.image}" alt="${product.name}" />
          <span class="name">${product.name}</span>
          <span class="price">$${product.price}</span>
          <input type="number" value="${product.quantity}" class="quantity" />
          <button class="remove">Eliminar</button>
        </div>
      `;
      document.querySelector('.cart-products').appendChild(productElement);
    });
  
    updateTotal();
  }
  
  function updateTotal() {
    let cart = JSON.parse(localStorage.getItem('cart')) || [];
    let total = cart.reduce((acc, product) => acc + product.price * product.quantity, 0);
    document.querySelector('.total').textContent = `$${total} MXN`;
  }
  
  document.addEventListener('DOMContentLoaded', () => {
    loadCart();
    document.querySelectorAll('.remove').forEach(button => {
      button.addEventListener('click', e => {
        const productId = e.target.closest('.product').dataset.id;
        removeProduct(productId);
      });
    });
  
    document.querySelectorAll('.quantity').forEach(input => {
      input.addEventListener('change', e => {
        const productId = e.target.closest('.product').dataset.id;
        const newQuantity = parseInt(e.target.value, 10);
        updateProductQuantity(productId, newQuantity);
      });
    });
  });
  
  function removeProduct(productId) {
    let cart = JSON.parse(localStorage.getItem('cart'));
    cart = cart.filter(product => product.id !== productId);
    localStorage.setItem('cart', JSON.stringify(cart));
    document.querySelector(`.product[data-id="${productId}"]`).remove();
    updateTotal();
  }
  
  function updateProductQuantity(productId, newQuantity) {
    let cart = JSON.parse(localStorage.getItem('cart'));
    let product = cart.find(p => p.id === productId);
  
    if (product) {
      product.quantity = newQuantity;
      localStorage.setItem('cart', JSON.stringify(cart));
      updateTotal();
    }
  }