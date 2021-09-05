import MessageRepository from "../repositories/MessageRepository";

class MessageService {
  async unrecognizedMessage(message): Promise<boolean> {
    return MessageRepository.unrecognizedMessage(message);
  }
}

export default new MessageService();
