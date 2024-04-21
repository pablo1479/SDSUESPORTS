import React, { useEffect } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';

const Home = () => {
    // Function to display a welcome message when the page loads
    const displayWelcomeMessage = () => {
        console.log("Welcome to the SDSU ESports Team website!");
    };

    // Function to handle navigation menu highlighting
    const highlightNavigation = () => {
        // Get the current page URL
        const currentPageUrl = window.location.href;

        // Get all the navigation links
        const navLinks = document.querySelectorAll("nav ul li a");

        // Loop through each navigation link
        navLinks.forEach(link => {
            // Check if the link href matches the current page URL
            if (link.href === currentPageUrl) {
                // Add a CSS class to highlight the current page link
                link.classList.add("active");
            }
        });
    };

    // Call the functions when the component mounts
    useEffect(() => {
        displayWelcomeMessage();
        highlightNavigation();
    }, []); // Empty dependency array ensures the effect runs only once

    return <div />;
};

export default Home;
