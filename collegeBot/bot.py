from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
from bot_brain.settings import agent as load_agent
logger = logging.getLogger(__name__)

def college_bot(message):
    print(type(message))
    print('Welcome to College Bot.Ask youe queries! ')
    responses = load_agent.handle_message(message)
    print(responses)
    return responses



if __name__ == '__main__':
	college_bot()
