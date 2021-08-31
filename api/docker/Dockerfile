FROM node:12-alpine

WORKDIR /src

COPY /api/package.json /api/yarn.lock /src/

RUN yarn install --production \
    && mv node_modules node_modules_prod \
    && yarn

COPY /api /src

RUN yarn tsc

FROM node:12-alpine

WORKDIR /app

COPY --from=0 /src/dist /app/dist
COPY --from=0 /src/node_modules_prod /app/node_modules
COPY /api/package.json /api/yarn.lock /app/

CMD node /app/dist/index.js