import React, { useEffect } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';

const Merch = () => {
    const sortItems = () => {
        const itemList = document.querySelector('.col-md-6 ul');
        const items = Array.from(itemList.children);
        items.sort((a, b) => a.textContent.localeCompare(b.textContent));
        itemList.innerHTML = '';
        items.forEach(item => {
            itemList.appendChild(item);
        });
    };

    useEffect(() => {
        sortItems();
    }, []);

    return <div />;
};

export default Merch;
