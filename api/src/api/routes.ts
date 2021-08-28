import express from "express";
import indexController from "./controllers/IndexController";
import FAQController from "./controllers/FAQController";
import Exception from "../core/exceptions/Exception";

const router = express.Router();

router.get("/", indexController.index);

const faqRouter = express.Router();
const itemRouter = express.Router({ mergeParams: true });

faqRouter.use("/faq", faqRouter, itemRouter);
faqRouter.get("/", FAQController.getFat);
faqRouter.get("/questions", FAQController.getFatQuestion);

router.get("/category", FAQController.getCategory);

router.all("*", () => {
  throw new Exception(404, "Page not found");
});

export default router;
