import { IFAQ, IFAQQuestion } from "../interfaces/IFAQ";

import Exception from "../exceptions/Exception";
import FAQRepository from "../repositories/FAQRepository";
import { ICategory } from "./../interfaces/IFAQ";

class FAQService {
  async getFAQs(payload): Promise<IFAQ[]> {
    return FAQRepository.getFAQs(payload);
  }

  async getFAQsQuestion(payload): Promise<IFAQQuestion[]> {
    return FAQRepository.getFAQsQuestion(payload);
  }

  async getCategoryFAQs(): Promise<ICategory[]> {
    return FAQRepository.getFAQCategories();
  }

  async healthCheck(): Promise<any> {
    const hc = await FAQRepository.healtChecking();

    if (hc) {
      return true;
    }

    throw new Exception(500, "Database is not ready");
  }
}

export default new FAQService();
