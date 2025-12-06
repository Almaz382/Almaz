import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random
from random import choice
Token = 'vk1.a.o_H4wJdw2C8nrf0KbmYDy6wvCsXcnvGXt-BfZP6ZHAdChQ-J5iOCf6kyRZFH5vh35oSu0UDXs8cvoEZVV6bB1fOpE_y5UxU7cBhdHvFDhxGws-Gz3m7lecKTfk6wNoTNga10O3OwAn5pRSKTNg5ux5BU1SLSljFBezsyk-mRwblg7Y56U8F68YPWeXp52bEs6XRE0ogPSUp_HhAG2xmbXQ'
vk_session = vk_api.VkApi(token = Token)
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()

vars = ['камень', "ножницы", "бумага"]
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text and str(event.text).lower() in vars:
        user = str(event.text).lower()
        if event.from_user:
            bot = choice(vars)
            vk.messages.send(user_id=event.user_id, message=bot, random_id = random.randint(1, 100000))
            out = None

            if user == 'камень':
                if bot == 'камень':
                    out = 'Ничья'
                elif bot == 'бумага':
                    out = 'Ты проиграл! (хахахахаах)'
                else: out = 'Ты победил :('
            
            if user == 'бумага':
                if bot == 'бумага':
                    out = 'Ничья'
                elif bot == 'ножницы':
                    out = 'Ты проиграл! (хахахахаах)'
                else: out = 'Ты победил :('

            if user == 'ножницы':
                if bot == 'ножницы':
                    out = 'Ничья'
                elif bot == 'камень':
                    out = 'Ты проиграл! (хахахахаах)'
                else: out = 'Ты победил :('
            
            vk.messages.send(user_id=event.user_id, message=out, random_id = random.randint(1, 100000))                       