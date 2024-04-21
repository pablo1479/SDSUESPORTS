

document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('registrationForm');

    form.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevents the form from submitting by default

        // Perform validation
        const firstName = document.getElementById('Fname').value.trim();
        const lastName = document.getElementById('Lname').value.trim();
        const email = document.getElementById('Semail').value.trim();
        const password = document.getElementById('Pword').value.trim();
        const studentId = document.getElementById('Sid').value.trim();

        // You can perform more complex validation here, this is just a basic example
        if (firstName === '' || lastName === '' || email === '' || password === '' || studentId === '') {
            alert('Please fill in all the required fields.');
        } else {
            // Form is valid, you can submit the form or perform further actions here
            alert('Form submitted successfully!');
            form.reset(); // Optionally, reset the form after successful submission
        }
    });
});
