import { NextFunction, Request, Response } from "express";

import Controller from "./Controller";
import MessageService from "../../core/services/MessageService";
import MessageValidator from "../validators/MessageValidator";

class MessageController extends Controller {
  async unrecognizedMessage(req: Request, res: Response, next: NextFunction) {
    try {
      const { message } = await MessageValidator.unrecognizedMessageValidate(
        req
      );

      const payload = await MessageService.unrecognizedMessage(message);

      super.response(res, {
        message: "Regristro adicionado com sucesso",
        payload,
      });
    } catch (err) {
      next(err);
    }
  }
}

export default new MessageController();
