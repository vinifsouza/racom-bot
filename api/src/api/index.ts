/* eslint-disable no-console */
import { API_PORT } from "../config";
import apiRouter from "./routes";
import express from "express";
import handleErrors from "./middleware/handleErrors";

const app = express();

app.use(express.json());

app.use("/", apiRouter);

app.use(handleErrors);

app.listen(5000, () => {
  console.log("API - Server Started on Port ", API_PORT, "🔥");
});
