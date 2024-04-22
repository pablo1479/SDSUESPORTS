<?php

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    
    if (isset($_POST['teamName']) && isset($_POST['teamLeaderName']) && isset($_POST['teamLeaderEmail']) && isset($_POST['gamesInterested']) && isset($_POST['teammateName'])) {
        
        
        $teamName = $_POST['teamName'];
        $teamLeaderName = $_POST['teamLeaderName'];
        $teamLeaderEmail = $_POST['teamLeaderEmail'];
        $gamesInterested = $_POST['gamesInterested'];
        $teammateNames = $_POST['teammateName'];

        
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
    
    header("Location: application.html");
    exit();
}
?>
