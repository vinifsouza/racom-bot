/* eslint-disable no-console */

import { API_PORT } from "../config";
import apiRouter from "./routes";
import cors from "cors";
import express from "express";
import handleErrors from "./middleware/handleErrors";

const app = express();

const corsOptions = {
  origin: "*",
  optionsSuccessStatus: 200,
  methods: "*",
  allowedHeaders: "*",
};

app.use(cors(corsOptions));

app.use(express.json());

app.use("/", apiRouter);

app.use(handleErrors);

app.listen(API_PORT, () => {
  console.log("API - Server Started on Port ", API_PORT, "🔥");
});
