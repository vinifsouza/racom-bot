import json
import requests

import yaml

from config import CHATBOT_CREDENTIALS_YML_PATH


def load_yml_existing(path):
    with open(path, 'r') as f:
        return yaml.safe_load(f)


def get_ngrok_url():
    url = "http://localhost:4040/api/tunnels"
    res = requests.get(url)
    res_unicode = res.content.decode("utf-8")
    res_json = json.loads(res_unicode)
    return res_json["tunnels"][0]["public_url"]


def main():
    yml_loaded = load_yml_existing(CHATBOT_CREDENTIALS_YML_PATH)

    ngrok_url = get_ngrok_url()
    ngrok_url = f'{ngrok_url}/webhooks/telegram/webhook'

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
