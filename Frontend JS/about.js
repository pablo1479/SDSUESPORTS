

// Function to display a welcome message when the page loads
function displayWelcomeMessage() {
    console.log("Welcome to the SDSU ESports Team website!");
}

// Function to handle navigation menu highlighting
function highlightNavigation() {
    // Get the current page URL
    var currentPageUrl = window.location.href;

    // Get all the navigation links
    var navLinks = document.querySelectorAll("nav ul li a");

    // Loop through each navigation link
    navLinks.forEach(function(link) {
        // Check if the link href matches the current page URL
        if (link.href === currentPageUrl) {
            // Add a CSS class to highlight the current page link
            link.classList.add("active");
        }
    });
}

// Call the functions when the DOM content is loaded
document.addEventListener("DOMContentLoaded", function() {
    // Display the welcome message
    displayWelcomeMessage();

    // Highlight the current page in the navigation menu
    highlightNavigation();
});