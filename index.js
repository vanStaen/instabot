const path = require("path");
const express = require("express");
const PORT = process.env.PORT || 8080;

// Init Express
const app = express();

// Set Static folder
app.use(express.static(path.join(__dirname, "public")));

// Static pointing to the logs
app.get("/log", (req, res) => {
  res.sendFile(path.join(__dirname, "log/insta_bot.log"));
});

// Endpoint routes handlers:
app.use("/accounts", require("./api/accounts"));

// Listen on a port
app.listen(PORT, () => console.log(`Server started on port ${PORT}`));
