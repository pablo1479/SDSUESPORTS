import React, { useState } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';

const Contact = () => {
    // State to manage form input values
    const [formData, setFormData] = useState({
        name: '',
        email: '',
        message: ''
    });

    // Function to handle form submission
    const handleSubmit = (event) => {
        event.preventDefault();
        
        // Access form data from state
        const { name, email, message } = formData;

        // Log form data
        console.log('Name:', name);
        console.log('Email:', email);
        console.log('Message:', message);

        // Clear form fields after submission
        setFormData({
            name: '',
            email: '',
            message: ''
        });
    };

    // Function to handle input change
    const handleChange = (event) => {
        const { name, value } = event.target;
        // Update form data state with new input value
        setFormData(prevState => ({
            ...prevState,
            [name]: value
        }));
    };

    return (
        <section id="contact">
            <h2>Contact Us</h2>
            
            <p>
                If you have any questions or feedback, 
                feel free to reach out to us using the form below:
            </p>
            
            <form onSubmit={handleSubmit}>
                <label htmlFor="name">Name:</label><br />
                <input 
                    type="text" 
                    id="name" 
                    name="name" 
                    value={formData.name} 
                    onChange={handleChange} 
                    required 
                /><br />
                <label htmlFor="email">Email:</label><br />
                <input 
                    type="email" 
                    id="email" 
                    name="email" 
                    value={formData.email} 
                    onChange={handleChange} 
                    required 
                /><br />
                <label htmlFor="message">Message:</label><br />
                <textarea 
                    id="message" 
                    name="message" 
                    rows="4" 
                    value={formData.message} 
                    onChange={handleChange} 
                    required 
                ></textarea><br />
                <input type="submit" value="Submit" />
            </form>
            
            <h2>Contacts:</h2>
            <ul>
                <li>Name: Robert McLintock, Email: Robert@example.com</li>
                <li>Name: Pablo Olivares, Email: Pablo@example.com</li>
                <li>Name: Brandon Reynolds, Email: Brandon@example.com</li>
                <li>Name: Alex Rivera, Email: Alex@example.com</li>
            </ul>
        </section>
    );
};

export default Contact;
