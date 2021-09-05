import { NextFunction, Request, Response } from "express";

import ConfigService from "../../core/services/ConfigService";
import Controller from "./Controller";

class IndexController extends Controller {
  async index(req: Request, res: Response, next: NextFunction) {
    try {
      const databaseStatus = await ConfigService.healthCheck();

      const data = {
        name: `ps-compasso-rasa-api`,
        version: "v1.0",
        author: "Vinícius Souza",
        repository: "https://github.com/vinifsouza/ps-compasso-rasa",
        database: {
          up: databaseStatus,
        },
      };

      super.response(res, data);
    } catch (err) {
      next(err);
    }
  }
}

export default new IndexController();
