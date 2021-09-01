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
    connectionTimeout: 10000, // milliseconds
    requestTimeout: 10000, // milliseconds
    options: {
      enableArithAbort: true,
    },
    pool: {
      min: 1,
      max: 2,
      acquireTimeoutMillis: 3000,
      evictionRunIntervalMillis: 60000,
      idleTimeoutMillis: 600000,
    },
  },
});

export default knex;
