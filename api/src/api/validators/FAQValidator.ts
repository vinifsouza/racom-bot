import * as Yup from "yup";

import Exception from "./../../core/exceptions/Exception";
import { IFAQValidate } from "./../../core/interfaces/IFAQ";
import { Request } from "express";

class FAQValidator {
  async faqValidate(req: Request): Promise<IFAQValidate> {
    const schema = Yup.object({
      id: Yup.number().optional(),
      question: Yup.string().optional(),
    });

    const payload = {
      id: req.query.id,
      question: req.query.question,
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

export default new FAQValidator();
