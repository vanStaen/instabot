const express = require("express");
const path = require("path");
const fs = require('fs');
const isAuth = require("./middleware/is-auth");


const PORT = process.env.PORT || 5008;
require("dotenv/config");

// Init Express
const app = express();

// Body Parser Middleware
app.use(express.json());
app.use(express.urlencoded({ extended: false }));

// Authorization Middleware
app.use(isAuth);

// Allow cross origin request
app.use((req, res, next) => {
  res.setHeader("Access-Control-Allow-Origin", "*");
  res.setHeader("Access-Control-Allow-Methods", "POST, GET, DELETE, PATCH, OPTIONS");
  res.setHeader("Access-Control-Allow-Headers", "Content-Type, Authorization");
  if (req.method === "OPTIONS") {
    return res.sendStatus(200);
  }
  next();
});

// Show logs
app.get("/log", function (req, res) {
  fs.readFile("./log/insta_bot.log", "utf8", function (err, html) {
    res.send(html);
  });
});


// Set up for React
app.use(express.static(path.join(__dirname, "build")));
app.get('/', (req, res) => { res.sendFile(path.join(__dirname, "build", "index.html")); });

// Router to API endpoints
app.use("/accounts", require("./api/accounts"));

// Listen on a port
app.listen(PORT, () => console.log(`Server started on port ${PORT}`));
