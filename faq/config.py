import os

API_PORT = 4444
DATABASE_HOST = os.environ.get('DATABASE_HOST') or 'http://localhost'
DATABASE_PORT = os.environ.get('DATABASE_PORT') or '3306'
DATABASE_USER = os.environ.get('DATABASE_USER') or 'root'
DATABASE_PASS = os.environ.get('DATABASE_PASS') or 'password'
DATABASE_NAME = os.environ.get('DATABASE_NAME') or 'rasa_db'

API_PORT = os.environ.get('API_PORT') or '4444'
