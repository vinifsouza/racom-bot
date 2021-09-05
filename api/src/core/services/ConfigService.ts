import ConfigRepository from "../repositories/ConfigRepository";
import Exception from "../exceptions/Exception";
import { IConfig } from "../interfaces/IConfig";

class ConfigService {
  async setConfig(field: string, value: string, app: string): Promise<boolean> {
    return ConfigRepository.setConfig(field, value, app);
  }

  async getConfig(field: string, app: string): Promise<IConfig> {
    return ConfigRepository.getConfig(field, app);
  }

  async healthCheck(): Promise<any> {
    const hc = await ConfigRepository.healtChecking();

    if (hc) {
      return true;
    }

    throw new Exception(500, "Database is not ready");
  }
}

export default new ConfigService();
