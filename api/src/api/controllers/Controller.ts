import { Response } from "express";

class Controller {
  public response(res: Response, data: any, status = 200) {
    return res.status(status).json({
      success: true,
      data,
    });
  }
}

export default Controller;
