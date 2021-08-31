from typing import Any, Text, Dict, List
import os
import requests

from rasa_sdk import Action, Tracker
from rasa_sdk.events import UserUtteranceReverted
from rasa_sdk.executor import CollectingDispatcher

FINISH_OPTIONS = [
    {'title': 'Dúvida sobre COVID', 'payload': '/intent_welcome'},
    {'title': 'Finalizar', 'payload': '/intent_finish'}
]

API_PORT = os.environ.get('API_PORT') or '4444'
API_HOST = os.environ.get('API_HOST') or 'http://localhost'
RANCOM_API_URL = f'http://{API_HOST}:{API_PORT}'


def get_response_by_question_id(id: int) -> str:
    req = requests.get(f'{RANCOM_API_URL}/faq', params={'id': id})

    return req.json()['data'][0]['answer']


class ActionDefaultFallback(Action):
    def name(self) -> Text:
        return 'action_default_fallback'

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        msg = 'Desculpe, não consegui compreender sua dúvida\n'
        msg += 'Por gentileza, tente novamente escrevendo de outra forma'

        dispatcher.utter_message(text=msg, buttons=FINISH_OPTIONS)

        # Revert user message which led to fallback.
        return [UserUtteranceReverted()]


class ActionWelcome(Action):
    def name(self) -> Text:
        return 'action_welcome'

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        msg = 'Olá, sou o RacomBot.\n'
        msg += 'Fui treinado para auxiliar em questões sobre COVID-19.\n'
        msg += 'Como posso ajudar hoje?'

        dispatcher.utter_message(text=msg)

        return []


class ActionAboutme(Action):
    def name(self) -> Text:
        return 'action_about_me'

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        about_me = 'Sou um bot desenvolvido por Vinícius Souza, '
        about_me += 'para o processo seletivo da Compasso UOL.'
        about_me += '\n\n'
        about_me += 'Fui treinado para responder dúvidas sobre COVID-19 '
        about_me += 'com base em informações da Fiocruz.'

        dispatcher.utter_message(text=about_me, buttons=FINISH_OPTIONS)

        return []


class ActionHelp(Action):
    def name(self) -> Text:
        return 'action_help'

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        message = 'Em que posso ajudar?'

        dispatcher.utter_message(text=message, buttons=FINISH_OPTIONS)

        return []


class RespondFaq(Action):
    def name(self) -> Text:
        return 'respond_faq'

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        message_user = tracker.latest_message
        message_user = message_user['response_selector']['faq']
        message_user = message_user['response']['intent_response_key']
        question_id = message_user.replace('faq/', '')

        message = get_response_by_question_id(question_id)

        dispatcher.utter_message(text=message)

        return []
