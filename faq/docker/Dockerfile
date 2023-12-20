FROM python:3.10.13

COPY /faq/requirements.txt requirements.txt
RUN pip install -r requirements.txt

ADD ./faq /faq

ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.9.0/wait /wait
RUN chmod +x /wait

WORKDIR /faq

CMD /wait && python /faq/main.py
