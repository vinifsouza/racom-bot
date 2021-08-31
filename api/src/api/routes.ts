// import Exception from "../core/exceptions/Exception";

import FAQController from "./controllers/FAQController";
import express from "express";
import indexController from "./controllers/IndexController";

const router = express.Router();

router.get("/", indexController.index);

router.get("/faq", FAQController.getFat);
router.get("/faq/questions", FAQController.getFatQuestion);

router.get("/category", FAQController.getCategory);

router.get("/health", FAQController.healthCheck);

// router.all("*", () => {
//   throw new Exception(404, "Page not found");
// });

export default router;
