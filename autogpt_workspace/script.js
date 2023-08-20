document.addEventListener('DOMContentLoaded', function() {
  fetch('menu.json')
    .then(response => response.json())
    .then(data => {
      const menuSection = document.getElementById('menu');
      const menuItems = data.menuItems;
      menuItems.forEach(item => {
        const menuItem = document.createElement('div');
        menuItem.innerHTML = `<h3>${item.name}</h3><p>${item.description}</p><p>Price: $${item.price.toFixed(2)}</p>`;
        menuSection.appendChild(menuItem);
      });
    })
    .catch(error => console.error('Error fetching menu data:', error));
});