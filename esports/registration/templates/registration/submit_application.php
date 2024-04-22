<?php
// Check if form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Check if all required fields are filled
    if (isset($_POST['teamName']) && isset($_POST['teamLeaderName']) && isset($_POST['teamLeaderEmail']) && isset($_POST['gamesInterested']) && isset($_POST['teammateName'])) {
        
        // Retrieve form data
        $teamName = $_POST['teamName'];
        $teamLeaderName = $_POST['teamLeaderName'];
        $teamLeaderEmail = $_POST['teamLeaderEmail'];
        $gamesInterested = $_POST['gamesInterested'];
        $teammateNames = $_POST['teammateName'];

        // Process the data as needed, such as storing it in a database or sending it via email
        // For now, let's just print the data
        echo "<h2>Application Submitted Successfully</h2>";
        echo "<p>Team Name: $teamName</p>";
        echo "<p>Team Leader Name: $teamLeaderName</p>";
        echo "<p>Team Leader Email: $teamLeaderEmail</p>";
        echo "<p>Games Interested In: $gamesInterested</p>";
        echo "<p>Team Members:</p>";
        echo "<ul>";
        foreach ($teammateNames as $name) {
            echo "<li>$name</li>";
        }
        echo "</ul>";
    } else {
        echo "All fields are required!";
    }
} else {
    // Redirect back to the form page if accessed directly
    header("Location: application.html");
    exit();
}
?>
