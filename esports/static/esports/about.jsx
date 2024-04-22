import React, { useEffect } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';

const About = () => {

    // Function to display welcome message
    const displayWelcomeMessage = () => {
        console.log("What we are about?");
    }

    // Function to highlight navigation
    const highlightNavigation = () => {
        const currentPageUrl = window.location.href;
        const navLinks = document.querySelectorAll("nav ul li a");

        navLinks.forEach((link) => {
            if (link.href === currentPageUrl) {
                link.classList.add("active");
            }
        });
    }
    // Use useEffect to execute functions after component is mounted
    useEffect(() => {
        displayWelcomeMessage();
        highlightNavigation();

        // Clean up function to remove event listeners or timers if needed
        return () => {
            // Perform cleanup here if necessary
        };
    }, []); // Empty dependency array means the effect runs only once after mounting

    return (
        <div>
            {/* Add your JSX content here */}
            <h1>About Us</h1>
            <p>Welcome to our website! We are...</p>
        </div>
    );
}

export default About;