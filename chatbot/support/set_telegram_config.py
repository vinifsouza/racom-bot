import json
import requests

import yaml

from config import CHATBOT_CREDENTIALS_YML_PATH, NGROK_API_URL, RANCOM_API_URL


def load_yml_existing(path):
    with open(path, 'r') as f:
        return yaml.safe_load(f)


def set_ngrok_url_to_api_config(ngrok_url):
    payload = {
        "field": 'ngrok_url',
        "value": str(ngrok_url),
        "app": 'chatbot'
    }

    headers = {"Content-Type": "application/json"}

    requests.post(f'{RANCOM_API_URL}/config', json=payload, headers=headers)

    return None


def get_ngrok_url():
    url = f'{NGROK_API_URL}/api/tunnels'
    res = requests.get(url)
    res_unicode = res.content.decode('utf-8')
    res_json = json.loads(res_unicode)
    return res_json['tunnels'][0]['public_url']


def main():
    yml_loaded = load_yml_existing(CHATBOT_CREDENTIALS_YML_PATH)

    ngrok_url = get_ngrok_url()

    set_ngrok_url_to_api_config(ngrok_url)

    ngrok_url = f'{ngrok_url}/webhooks/telegram/webhook'

    ngrok_url = ngrok_url.replace('http://', 'https://')

    yml_loaded['telegram']['webhook_url'] = ngrok_url

    yaml.preserve_quotes = False
    with open(CHATBOT_CREDENTIALS_YML_PATH, 'w+') as credentials_output:
        yaml.dump(
            yml_loaded,
            credentials_output,
            default_flow_style=False,
            sort_keys=False,
            allow_unicode=True,
            indent=2
        )

    return None
