import React, { useState } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';

const Application = () => {
    // State to manage team members
    const [teamMembers, setTeamMembers] = useState([]);

    // Function to add a new member to the team
    const addMember = () => {
        setTeamMembers([...teamMembers, '']);
    };

    return (
        <div className="container">
            <form>
                <div className="mb-3">
                    <label htmlFor="teamName" className="form-label">Team Name:</label>
                    <input type="text" className="form-control" id="teamName" name="teamName" required />
                </div>
                <div className="mb-3">
                    <label htmlFor="teamLeaderName" className="form-label">Team Leader Name:</label>
                    <input type="text" className="form-control" id="teamLeaderName" name="teamLeaderName" required />
                </div>
                {/* Add other form fields here */}

                {/* Team Members */}
                <div className="mb-3" id="teamMembers">
                    <label htmlFor="teamMembers" className="form-label">Team Members:</label>
                    {/* Map through team members and display input for each */}
                    {teamMembers.map((member, index) => (
                        <div className="team-member" key={index}>
                            <input type="text" className="form-control" name="teammateName[]" placeholder="Teammate Name" />
                        </div>
                    ))}
                </div>
                <button type="button" className="btn btn-primary mb-3" onClick={addMember}>Add Member</button>
                <input type="submit" className="btn btn-success" value="Submit Application" />
            </form>
        </div>
    );
};

export default Application;


