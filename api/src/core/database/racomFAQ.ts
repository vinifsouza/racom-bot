import Knex from "knex";
import { resolve } from "path";
import { DATABASE_PATH } from "../../config";

const knex = Knex({
  client: "sqlite3",
  connection: {
    filename: resolve(DATABASE_PATH),
  },
  useNullAsDefault: true,
});

export default knex;
