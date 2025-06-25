# Модуль первоначальной решистрации юзер-бота
import logging
import os

from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler

log = logging.getLogger(__name__)
number = '79038272699'

app = Client(number, os.environ['API_ID'], os.environ['API_HASH'])
limit = 10  # Сколько последних сообщений получить


async def main():
    async with app:
        # "me" refers to your own chat (Saved Messages)
        async for message in app.get_chat_history(chat_id=-1002611854380, limit=limit):
            print(message)


app.run(main())