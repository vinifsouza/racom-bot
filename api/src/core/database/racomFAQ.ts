import {
  DATABASE_HOST,
  DATABASE_NAME,
  DATABASE_PASS,
  DATABASE_USER,
} from "../../config";

import Knex from "knex";

const knex = Knex({
  client: "mysql",
  connection: {
    host: DATABASE_HOST,
    user: DATABASE_USER,
    password: DATABASE_PASS,
    database: DATABASE_NAME,
  },
  useNullAsDefault: true,
});

export default knex;
