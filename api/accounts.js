const express = require("express");
const router = express.Router();
const { Client } = require("pg");

// Init Postgres
const client = new Client({
  connectionString: process.env.DATABASE_URL,
  ssl: true,
});
process.env.NODE_TLS_REJECT_UNAUTHORIZED = 0; // This bypasses the SSL verification

// Connect to Postgres
client.connect((err) => {
  if (err) {
    console.error("connection error", err.stack);
  } else {
    console.log("Activity API:", "Connected to postgres db on Heroku!");
  }
});

// Init Postgres
const clientAWS = new Client({
  connectionString: process.env.DATABASE_URL_AWS,
  ssl: true,
});
process.env.NODE_TLS_REJECT_UNAUTHORIZED = 0; // This bypasses the SSL verification

// Connect to Postgres
clientAWS.connect((err) => {
  if (err) {
    console.error("connection error", err.stack);
  } else {
    console.log("Activity API:", "Connected to postgres db on AWS!");
  }
});

// GET all data from config_accounts_insta
router.get("/", async (req, res) => {
  try {
    const data = await client.query("SELECT * FROM config_accounts_insta");
    res.status(201).json(data.rows);
  } catch (err) {
    res.status(400).json({
      error: `${err})`,
    });
  }
});

router.get("/count/:account/", async (req, res) => {
  try {
    const query =
      "SELECT COUNT(*) FROM public.userlist_" + req.params.account;
    const dataDetail = await clientAWS.query(query);
    res.status(201).json(dataDetail.rows);
  } catch (err) {
    res.status(400).json({
      error: `${err})`,
    });
  }
});

// UPDATE account alive
router.post("/alive", async (req, res) => {
  try {
    const query = `UPDATE config_accounts_insta SET alive='${req.body.alive}' WHERE username='${req.body.username}'`;
    await client.query(query);
    res.status(201).json({ message: "Success!" });
  } catch (err) {
    res.status(400).json({
      error: `${err})`,
    });
  }
});

// UPDATE account active
router.post("/active", async (req, res) => {
  try {
    const query = `UPDATE config_accounts_insta SET active='${req.body.active}' WHERE username='${req.body.username}'`;

    await client.query(query);
    res.status(201).json({ message: "Success!" });
  } catch (err) {
    res.status(400).json({
      error: `${err})`,
    });
  }
});

module.exports = router;
