import os

API_PORT = os.environ.get('API_PORT') or '4444'
API_HOST = os.environ.get('API_HOST') or 'http://localhost'
RANCOM_API_URL = f'http://{API_HOST}:{API_PORT}'

NGROK_HOST = os.environ.get('NGROK_HOST') or 'http://localhost'
NGROK_PORT = os.environ.get('NGROK_PORT') or '4040'
NGROK_API_URL = f'http://localhost:{NGROK_PORT}'

CHATBOT_NLU_YML_PATH = './data/nlu.yml'
CHATBOT_DOMAIN_YML_PATH = 'domain.yml'
CHATBOT_CREDENTIALS_YML_PATH = 'credentials.yml'
