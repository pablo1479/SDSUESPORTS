function displayWelcomeMessage() {
    console.log("What we are about?");
}

function highlightNavigation() {
    var currentPageUrl = window.location.href;
    var navLinks = document.querySelectorAll("nav ul li a");
    navLinks.forEach(function(link) {

        if (link.href === currentPageUrl) {
            link.classList.add("active");
        }
    });
}

document.addEventListener("DOMContentLoaded", function() {

    displayWelcomeMessage();

    highlightNavigation();
});
