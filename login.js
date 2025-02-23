const express = require("express");
const bodyParser = require("body-parser");

const app = express();
const PORT = 3000;

app.use(bodyParser.json());
app.use(express.static("public"));

app.post("/login", (req, res) => {
    const { name, email, password, role } = req.body;

    if (email === "test@example.com" && password === "password123") {
        res.send(`Login successful! Welcome, ${name} (${role})`);
    } else {
        res.status(401).send("Invalid credentials");
    }
});

app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});
