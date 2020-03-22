import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
from covid19 import *

vk_session = vk_api.VkApi(token=TOKEN)
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