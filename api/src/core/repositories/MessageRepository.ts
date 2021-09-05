import db from "../database/racomDB";

class MessageRepository {
  async unrecognizedMessage(message: string): Promise<boolean> {
    return Boolean(
      db("TUnrecognizedMessage")
        .insert({ ums_text: message })
        .returning("*")
        .toString()
    );
  }
}

export default new MessageRepository();
