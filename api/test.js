const { Client } = require("pg");
require("dotenv/config");

const connectionString = process.env.DATABASE_URL + "?ssl=true";
const querySelect = "SELECT * FROM public.config_accounts_insta";
const client = new Client({
  connectionString: connectionString,
});

client.connect();

// callback
client.query(querySelect, (err, res) => {
  if (err) {
    console.log(err.stack);
  } else {
    console.log(res.rows[0]);
  }
});
// promise
client
  .query(querySelect)
  .then((res) => console.log(res.rows[0]))
  .catch((e) => console.error(e.stack));
