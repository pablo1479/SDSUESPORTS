document.addEventListener('DOMContentLoaded', function() {
    function openStream(event) {
        event.preventDefault();
        const streamURL = event.target.href;
        window.open(streamURL, '_blank');
    }

    const streamLinks = document.querySelectorAll('.midcol ul li a');
    streamLinks.forEach(link => {
        link.addEventListener('click', openStream);
    });
});
