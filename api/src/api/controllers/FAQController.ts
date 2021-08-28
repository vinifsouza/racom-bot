import { Request, Response, NextFunction } from "express";
import FAQService from "../../core/services/FAQService";
import FAQValidator from "../validators/FAQValidator";
import Controller from "./Controller";

class FAQController extends Controller {
  async getFat(req: Request, res: Response, next: NextFunction) {
    try {
      const payload = await FAQValidator.faqValidate(req);

      const data = await FAQService.getFAQs(payload);

      super.response(res, data);
    } catch (err) {
      next(err);
    }
  }

  async getFatQuestion(req: Request, res: Response, next: NextFunction) {
    try {
      const payload = await FAQValidator.faqValidate(req);

      const data = await FAQService.getFAQsQuestion(payload);

      super.response(res, data);
    } catch (err) {
      next(err);
    }
  }

  async getCategory(req: Request, res: Response, next: NextFunction) {
    try {
      const data = await FAQService.getCategoryFAQs();
      super.response(res, data);
    } catch (err) {
      next(err);
    }
  }
}

export default new FAQController();
