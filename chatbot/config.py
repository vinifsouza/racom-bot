import os

API_PORT = os.environ.get('API_PORT') or '4444'
RANCOM_API_URL = f'http://localhost:{API_PORT}'

CHATBOT_NLU_YML_PATH = './data/nlu.yml'
CHATBOT_DOMAIN_YML_PATH = 'domain.yml'
CHATBOT_CREDENTIALS_YML_PATH = 'credentials.yml'
