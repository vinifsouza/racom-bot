import express from "express";
import indexController from "./controllers/IndexController";
import FAQController from "./controllers/FAQController";
import Exception from "../core/exceptions/Exception";

const router = express.Router();

router.get("/", indexController.index);

router.get("/faq", FAQController.getFat);
router.get("/faq/questions", FAQController.getFatQuestion);

router.get("/category", FAQController.getCategory);

router.all("*", () => {
  throw new Exception(404, "Page not found");
});

export default router;
