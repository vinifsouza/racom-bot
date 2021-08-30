FROM python:3.7

COPY /faq/requirements.txt requirements.txt
RUN pip install -r requirements.txt

ADD . /faq

WORKDIR /faq

CMD python /faq/main.py