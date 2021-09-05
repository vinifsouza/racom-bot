import { IFAQ, IFAQQuestion } from "../interfaces/IFAQ";

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
}

export default new FAQService();
