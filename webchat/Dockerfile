FROM node:18.19.0-alpine

ADD /webchat /webchat

WORKDIR /webchat

ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.9.0/wait /wait
RUN chmod +x /wait

CMD /wait && yarn install && yarn start
