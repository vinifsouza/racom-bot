FROM python:3.13.0a3

COPY /chatbot/requirements.txt requirements.txt
RUN pip install -r requirements.txt

WORKDIR /chatbot

ADD ./chatbot /chatbot

ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.9.0/wait /wait
RUN chmod +x /wait

WORKDIR /chatbot

CMD /wait && python /chatbot/main.py && rasa train && rasa run -p 5005 -m /chatbot/models \
    --credentials /chatbot/credentials.yml \
    --enable-api --endpoints /chatbot/endpoints.yml --cors "*"
