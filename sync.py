# Модуль скачивания картинок и видео из телеграм-чата/канала
import asyncio
import logging
import os
from pathlib import Path
from pyrogram import Client, filters
from pyrogram.enums import MessageMediaType
from pyrogram.handlers import MessageHandler

# Подключаемся к БД.
# Определяем настройки подключения к телеграм.
# Определяем номера чатов, откуда надо скачать данные.
# Определяем облака, куда надо загрузить данные

log = logging.getLogger(__name__)
number = os.environ['NUMBER']
app = Client(number, os.environ['API_ID'], os.environ['API_HASH'], workdir='sessions')
CHAT_ID = os.environ['CHAT_ID']

DOWNLOAD_PATH = Path(f'downloads/{CHAT_ID}')
if not DOWNLOAD_PATH.exists():
    DOWNLOAD_PATH.parent.mkdir(parents=True, exist_ok=True)
limit = 10  # Сколько последних сообщений получить


async def download_file(file_id: str, file_unique_id:str, file_ext: str, sub_dir: str):
    store_path = DOWNLOAD_PATH / Path(sub_dir)
    if not store_path.exists():
        store_path.mkdir(parents=True, exist_ok=True)
    file_path = store_path / Path(f'{file_unique_id}.{file_ext}')
    if file_path.exists() and file_path.stat().st_size > 0:
        log.info(f'Файл {file_unique_id} в {file_path} уже был скачан ранее.')
        return
    log.info(f'Скачиваем файл {file_unique_id}...')
    file_data = await app.download_media(file_id, in_memory=True)
    file_bytes = bytes(file_data.getbuffer())
    with open(file_path, "wb") as file:
        file.write(file_bytes)
    log.info(f'Скачан файл {file_unique_id} в {file_path}')


async def main():
    # print('Найдены диалоги:')
    # async for dialog in app.get_dialogs():
    #     print(f'id= {dialog.chat.id} name = {dialog.chat.first_name or dialog.chat.title}')
    offset_id = 0
    while True:
        async for message in app.get_chat_history(chat_id=CHAT_ID, limit=limit):
            print(message)
            if message.outgoing:
                continue
            #  TODO: 1. учитывать  "media_group_id": 14007559369261426 2. Учитывать подпись к посту
            if message.media == MessageMediaType.PHOTO:
                sub_dir = f'{message.date.strftime('%Y-%m-%d')}/{message.id}'
                photo = message.photo
                file_unique_id = photo.file_unique_id
                await download_file(photo.file_id, file_unique_id, 'jpg', sub_dir)


app.start()
app.run(main())
app.stop()

# offset_id = 0
# while True:
#     messages = await app.get_messages(chat_id=-1002611854380, message_ids = [2])
#     if not messages:  # Если сообщений больше нет
#         break
#     for message in messages:
#         print(message)
#         # print(f"Сообщение ID: {message.id}, Текст: {message.text or 'Нет текста'}")
#     offset_id = messages[-1].id  # Смещение для следующего запроса
# file = await app.download_media(file_id, in_memory=True)
# print(file)


# app.start()
#app.send_message('@mihmig', f'Юзербот: {number}')
# app.send_message(-4739990075, f'Юзербот: {number}')

