const express = require("express");
const bodyParser = require("body-parser");
const app = express();
const mysql = require("mysql");

//parse apllication/json
app.use(bodyParser.json());

//create database connection
const conn = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "",
  database: "go_coba",
});

//connect to databasse
conn.connect((err) => {
  if (err) throw err;
  console.log("Mysql Connected...");
});

//tampilkan data product
app.get("/getProducts", (req, res) => {
  let sql = "SELECT * FROM  products";
  let query = conn.query(sql, (err, results) => {
    if (err) throw err;
    res.send(JSON.stringify({ status: 200, error: null, response: results }));
  });
});

app.listen(3000, () => {
  console.log("Server Start On port 3000....");
});
