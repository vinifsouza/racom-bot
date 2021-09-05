const WEBCHAT_PORT = process.env.WEBCHAT_PORT || 4445;
const WEBCHAT_HOST = process.env.WEBCHAT_HOST || "127.0.0.1";

const express = require("express");
const app = express();

app.use(express.static("./"));

app.get("/", function (req, res) {
  res.render("index.html");
});

app.listen(WEBCHAT_PORT, WEBCHAT_HOST);
console.log("WebChat - Server Started on Port ", WEBCHAT_PORT, "🔥");
