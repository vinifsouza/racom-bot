from chatbot.config import RANCOM_API_URL
import requests

from chatbot.config import RANCOM_API_URL


def get_response_by_question_id(id: int) -> str:
    req = requests.get(RANCOM_API_URL, params={
        'id': id
    })

    return req.json()['data'][0]
