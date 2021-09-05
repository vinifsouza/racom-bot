import * as Yup from "yup";

import { IConfig, IGetConfigRequest } from "./../../core/interfaces/IConfig";

import Exception from "./../../core/exceptions/Exception";
import { Request } from "express";

class ConfigValidator {
  async setConfigValidate(req: Request): Promise<IConfig> {
    const schema = Yup.object({
      field: Yup.string().required(),
      value: Yup.string().required(),
      app: Yup.string().required(),
    });

    const payload = {
      field: String(req.body.field),
      value: String(req.body.value),
      app: String(req.body.app),
    };

    return schema.validate(payload, { abortEarly: false }).catch((err) => {
      const errors = {};

      err.inner.forEach((error) => {
        errors[error.path] = error.message;
      });

      throw new Exception(400, errors);
    });
  }

  async getConfigValidate(req: Request): Promise<IGetConfigRequest> {
    const schema = Yup.object({
      reqField: Yup.string().required("field is a required field"),
      reqApp: Yup.string().required("app is a required field"),
    });

    const payload = {
      reqField: req.query.field,
      reqApp: req.query.app,
    };

    return schema.validate(payload, { abortEarly: false }).catch((err: any) => {
      const errors = {};

      err.inner.forEach((error) => {
        errors[error.path] = error.message;
      });

      throw new Exception(400, errors);
    });
  }
}

export default new ConfigValidator();
