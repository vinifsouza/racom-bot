import ConfigController from "./controllers/ConfigController";
import FAQController from "./controllers/FAQController";
import MessageController from "./controllers/MessageController";
import express from "express";
import indexController from "./controllers/IndexController";

const router = express.Router();

router.get("/", indexController.index);

router.get("/faq", FAQController.getFat);
router.get("/faq/questions", FAQController.getFatQuestion);
router.get("/category", FAQController.getCategory);

router.post("/config", ConfigController.setConfig);
router.get("/config", ConfigController.getConfig);
router.get("/health", ConfigController.healthCheck);

router.post("/message/unrecognized", MessageController.unrecognizedMessage);

export default router;
