import * as Yup from "yup";

import Exception from "./../../core/exceptions/Exception";
import { Request } from "express";

class MessageValidator {
  async unrecognizedMessageValidate(req: Request): Promise<any> {
    const schema = Yup.object({
      message: Yup.string().required(),
    });

    const payload = {
      message: String(req.body.message),
    };

    return schema.validate(payload, { abortEarly: false }).catch((err) => {
      const errors = {};

      err.inner.forEach((error) => {
        errors[error.path] = error.message;
      });

      throw new Exception(400, errors);
    });
  }
}

export default new MessageValidator();
