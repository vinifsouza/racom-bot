import { IConfig } from "../interfaces/IConfig";
import db from "../database/racomDB";

class ConfigRepository {
  async setConfig(field: string, value: string, app: string): Promise<boolean> {
    return Boolean(
      db("TConfig")
        .insert({
          cfg_field: field,
          cfg_value: value,
          cfg_app: app,
        })
        .then()
        .catch(console.log)
    );
  }

  async getConfig(field: string, app: string): Promise<IConfig> {
    return db("TConfig")
      .select("cfg_field AS field", "cfg_value AS value", "cfg_app AS app")
      .where("cfg_field", field)
      .andWhere("cfg_app", app)
      .first();
  }

  async healtChecking(): Promise<any> {
    return db("information_schema.schemata").select(1);
  }
}

export default new ConfigRepository();
