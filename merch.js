document.addEventListener('DOMContentLoaded', function() {

    function sortItems() {

        const itemList = document.querySelector('.col-md-6 ul');
        const items = Array.from(itemList.children);
        items.sort((a, b) => a.textContent.localeCompare(b.textContent));
        itemList.innerHTML = '';
        items.forEach(item => {
            itemList.appendChild(item);
        });
    }

    sortItems();
});
