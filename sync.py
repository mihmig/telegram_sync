# Модуль первоначальной решистрации юзер-бота
import asyncio
import logging
import os

from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler

log = logging.getLogger(__name__)
number = '79038272699'
app = Client(number, os.environ['API_ID'], os.environ['API_HASH'])

async def download_file(file_id: str):
    # offset_id = 0
    # while True:
    #     messages = await app.get_messages(chat_id=-1002611854380, message_ids = [2])
    #     if not messages:  # Если сообщений больше нет
    #         break
    #     for message in messages:
    #         print(message)
    #         # print(f"Сообщение ID: {message.id}, Текст: {message.text or 'Нет текста'}")
    #     offset_id = messages[-1].id  # Смещение для следующего запроса
    # file = await app.download_media(file_id)
                                     AgACAgIAAyEFAASbrbwsAAMCaFxfRJ7HAr90JvA6TQH8VVVmS6cAAqv0MRsQB-FKd7oHxHS2XXMACAEAAwIAA3gABx4E
    file = await app.download_media("AgACAgIAAyEFAASbrbwsAAMCaFxOvrSB3zqchiffd5Soe7pM7EYAAqv0MRsQB-FKd7oHxHS2XXMACAEAAwIAA3gABx4E")
    print(file)
    # file = await app.download_media(file_id, in_memory = True)
    # file_bytes = bytes(file.getbuffer())
    # file_path = f'downloads/{file.name}'
    # with open(file_path, "wb") as file:
    #     file.write(file_bytes)

# app.start()
#app.send_message('@mihmig', f'Юзербот: {number}')
# app.send_message(-4739990075, f'Юзербот: {number}')
file_id = "AgACAgIAAyEFAASbrbwsAAMCaFxOvrSB3zqchiffd5Soe7pM7EYAAqv0MRsQB-FKd7oHxHS2XXMACAEAAwIAA3gABx4E"
app.run(download_file(file_id))
# app.stop()
# try:
#     asyncio.get_event_loop().run_forever()
# except KeyboardInterrupt:
#     log.info('Остановка бота...')
# finally:
#     app.stop()
