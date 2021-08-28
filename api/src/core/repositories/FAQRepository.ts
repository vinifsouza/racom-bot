import db from "../database/RacomFAQ";
import { ICategory, IFAQ, IFAQQuestion } from "../interfaces/IFAQ";

class FAQRepository {
  async getFAQCategories(): Promise<ICategory[] | []> {
    return db("TFAQCategory").select("cat_id AS id", "cat_name AS name");
  }

  async getFAQs(payload): Promise<IFAQ[] | []> {
    const { id, question } = payload;

    return db("TFAQ")
      .select(
        "faq_id AS id",
        "faq_question AS question",
        "faq_answer AS answer",
        "faq_category AS category"
      )
      .modify((queryBuilder: any) => {
        if (id) {
          queryBuilder.where("faq_id", id);
        }

        if (question) {
          queryBuilder.where("faq_question", "like", `%${question}%`);
        }
      });
  }

  async getFAQsQuestion(payload): Promise<IFAQQuestion[] | []> {
    const { id, question } = payload;

    return db("TFAQ")
      .select("faq_id AS id", "faq_question AS question")
      .modify((queryBuilder: any) => {
        if (id) {
          queryBuilder.where("faq_id", id);
        }

        if (question) {
          queryBuilder.where("faq_question", "like", `%${question}%`);
        }
      });
  }
}

export default new FAQRepository();
