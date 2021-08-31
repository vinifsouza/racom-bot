import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # nopep8
from chatbot.support import generate_intent_nlu
from chatbot.support import set_telegram_config

generate_intent_nlu.main()
set_telegram_config.main()
