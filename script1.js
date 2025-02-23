document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();

    // Get user inputs
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const role = document.getElementById('role').value;

    // Perform basic validation
    if (name === "" || email === "" || password === "") {
        alert("Please fill out all fields.");
        return;
    }

    // Simulate form submission
    console.log("Form Submitted!");
    console.log("Name: " + name);
    console.log("Email: " + email);
    console.log("Password: " + password);
    console.log("Role: " + role);

    // You can add an AJAX request to send the data to the server here.
    // Example:
    // fetch('/login', {
    //     method: 'POST',
    //     body: JSON.stringify({ name, email, password, role }),
    //     headers: {
    //         'Content-Type': 'application/json'
    //     }
    // })
    // .then(response => response.json())
    // .then(data => console.log(data))
    // .catch(error => console.log(error));
});
