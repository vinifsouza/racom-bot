import { NextFunction, Request, Response } from "express";

import ConfigService from "../../core/services/ConfigService";
import ConfigValidator from "../validators/ConfigValidator";
import Controller from "./Controller";

class ConfigController extends Controller {
  async setConfig(req: Request, res: Response, next: NextFunction) {
    try {
      const { field, value, app } = await ConfigValidator.setConfigValidate(
        req
      );

      await ConfigService.setConfig(field, value, app);

      super.response(
        res,
        { message: "Configuration created successfully" },
        201
      );
    } catch (err) {
      next(err);
    }
  }

  async getConfig(req: Request, res: Response, next: NextFunction) {
    try {
      const { reqField, reqApp } = await ConfigValidator.getConfigValidate(req);

      const { field, value, app } = await ConfigService.getConfig(
        reqField,
        reqApp
      );

      super.response(res, { field, value, app });
    } catch (err) {
      next(err);
    }
  }

  async healthCheck(req: Request, res: Response, next: NextFunction) {
    try {
      const databaseStatus = await ConfigService.healthCheck();

      super.response(res, { status: databaseStatus });
    } catch (err) {
      next(err);
    }
  }
}

export default new ConfigController();
