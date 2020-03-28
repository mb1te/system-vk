import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
from covid19 import * 

vk_session = vk_api.VkApi(token='95828ed40c8fa5afcc922fd9e004e7a4ae4d32647fcdd59ebf7ff66f778a921a760bde7808262df480a32')
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, '171143945') #id группы

def rand():
    return random.randint(1, 10**12)

def send_message(chat_id, text):
    vk.messages.send(chat_id=chat_id, message=text, random_id=rand())

for event in longpoll.listen():
    if (event.type == VkBotEventType.MESSAGE_NEW):
        if (event.obj.text == 'covid инфа'):
            send_message(event.chat_id, get_covid(False))
        if (event.obj.text == 'covid инфа детально'):
            send_message(event.chat_id, get_covid(True))