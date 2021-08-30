import yaml
import requests


from chatbot.config import CHATBOT_NLU_YML_PATH, RANCOM_API_URL


def load_yml_existing(path):
    with open(path, 'r') as f:
        return yaml.safe_load(f)


def get_faq_questions():
    req = requests.get(f'{RANCOM_API_URL}/faq/questions')

    return req.json()['data']


def generate_intents_ymy(data_json, data_yml_as_json=None):
    data = {
        'version': '2.0',
        'nlu': []
    }

    intent_list = []

    if data_yml_as_json:
        for item in data_yml_as_json['nlu']:
            obj = {
                'intent': item['intent'],
                'examples': item['examples']
            }

            data['nlu'].append(obj)
            intent_list.append(item['intent'])

    for item in data_json:
        obj = {
            'intent': f'faq/{item["id"]}',
            'examples': f'- {item["question"]}'
        }

        intent_list.append(obj['intent'])
        data['nlu'].append(obj)

    return data, intent_list


def main():
    questions = get_faq_questions()
    yml_loaded = load_yml_existing(CHATBOT_NLU_YML_PATH)

    update_intents, _ = generate_intents_ymy(questions, yml_loaded)

    yaml.preserve_quotes = False
    with open(CHATBOT_NLU_YML_PATH, 'w+') as nlu_output:
        yaml.dump(
            update_intents,
            nlu_output,
            default_flow_style=False,
            sort_keys=False,
            allow_unicode=True,
            indent=2)


if __name__ == '__main__':
    main()
