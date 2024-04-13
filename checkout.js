document.addEventListener('DOMContentLoaded', function () {
    const cartSummary = document.getElementById('cartSummary');
    const finalizePurchase = document.getElementById('finalizePurchase');
    const miauSound = document.getElementById('miauSound');
    let cart = JSON.parse(localStorage.getItem('cart') || '[]');

    cart.forEach(item => {
        let itemElement = document.createElement('p');
        itemElement.textContent = `${item.name} - $${item.price} x ${item.quantity}`;
        cartSummary.appendChild(itemElement);
    });

    finalizePurchase.addEventListener('click', () => {
        miauSound.play();
        alert('Gracias por tu compra!');
        localStorage.clear(); // Opcional: limpiar carrito después de la compra
    });
});

