import requests


def get_response_by_question_id(id: int) -> str:
    req = requests.get('http://localhost:4444/faq', params={'id': id})

    return req.json()['data'][0]['answer']
