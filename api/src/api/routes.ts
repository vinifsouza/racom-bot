import express from "express";
import indexController from "./controllers/IndexController";
import Exception from "../core/exceptions/Exception";

const router = express.Router();

router.get("/", indexController.index);

router.all("*", () => {
  throw new Exception(404, "Page not found");
});

export default router;
