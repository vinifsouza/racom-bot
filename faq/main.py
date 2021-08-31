import os
import sys
import json
from pymysql import IntegrityError

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # nopep8
from scrap.main import start_scrap
from database.build_db import CoreDatabase

print('Building database')
database = CoreDatabase()
database.build_schema()

print('Start scraping')
start_scrap()


with open('faq-scraping.json') as f:
    faqs = json.load(f)

for cat in faqs['categories']:
    database.insert_category_row(cat['id'], cat['name'])

for faq in faqs['articles']:
    try:
        database.insert_faq_row(
            faq['question'],
            faq['answer'],
            faq['answer_html'],
            faq['category_id']
        )
    except IntegrityError as e:
        if not 'Duplicate' in str(e):
            raise e

print('Database built and updated successfully')
