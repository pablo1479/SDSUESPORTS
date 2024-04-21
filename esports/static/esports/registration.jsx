import React, { useState } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';

const Registration = () => {
    const [formData, setFormData] = useState({
        firstName: '',
        lastName: '',
        email: '',
        password: '',
        studentId: ''
    });

    const handleSubmit = (event) => {
        event.preventDefault(); // Prevents the form from submitting by default

        // Perform validation
        const { firstName, lastName, email, password, studentId } = formData;

        // You can perform more complex validation here, this is just a basic example
        if (firstName === '' || lastName === '' || email === '' || password === '' || studentId === '') {
            alert('Please fill in all the required fields.');
        } else {
            // Form is valid, you can submit the form or perform further actions here
            alert('Form submitted successfully!');
            setFormData({ // Optionally, reset the form after successful submission
                firstName: '',
                lastName: '',
                email: '',
                password: '',
                studentId: ''
            });
        }
    };

    const handleChange = (event) => {
        const { name, value } = event.target;
        setFormData(prevState => ({
            ...prevState,
            [name]: value
        }));
    };

    return (
        <div className="container">
            <form onSubmit={handleSubmit}>
                <label htmlFor="Fname">First Name:</label>
                <input type="text" id="Fname" name="firstName" value={formData.firstName} onChange={handleChange} required />

                <label htmlFor="Lname">Last Name:</label>
                <input type="text" id="Lname" name="lastName" value={formData.lastName} onChange={handleChange} required />

                <br /><br />
                <label htmlFor="Semail">Student Email:</label>
                <input type="text" id="Semail" name="email" value={formData.email} onChange={handleChange} required />

                <label htmlFor="Pword">Password:</label>
                <input type="password" id="Pword" name="password" value={formData.password} onChange={handleChange} required />

                <br /><br />
                <label htmlFor="Sid">Student ID:</label>
                <input type="text" id="Sid" name="studentId" value={formData.studentId} onChange={handleChange} required />

                <input type="submit" value="Submit" />
            </form>
        </div>
    );
};

export default Registration;
