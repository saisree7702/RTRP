<?php
session_start();

// Database connection
$servername = "localhost";  // Change if needed
$username = "root";  // Your database username
$password = "";  // Your database password
$dbname = "freelance";  // Your database name

$conn = new mysqli($servername, $username, $password, $dbname);

// Check for errors
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Get form data
$role = $_POST['role'];
$name = $_POST['name'];
$email = $_POST['email'];
$password = password_hash($_POST['password'], PASSWORD_DEFAULT); // Hashing the password for security

// Insert into the database
$sql = "INSERT INTO login (role, name, email, password) VALUES (?, ?, ?, ?)";
$stmt = $conn->prepare($sql);
$stmt->bind_param("ssss", $role, $name, $email, $password);

if ($stmt->execute()) {
    // Redirect to login page with success message
    $_SESSION['message'] = "Registered successfully! Please log in.";
    header("Location: login.php");
    exit();
} else {
    echo "Error: " . $stmt->error;
}

$stmt->close();
$conn->close();
?>
