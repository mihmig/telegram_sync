# Модуль первоначальной регистрации юзер-бота
import asyncio
import logging
import os

from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler

log = logging.getLogger(__name__)
number = '79159814154'

app = Client(number, os.environ['API_ID'], os.environ['API_HASH'], workdir='sessions')

@app.on_message()
async def echo(client, message):
    print(message)
    app.read_chat_history(message.chat.id)
    await app.send_message(chat_id=message.chat.id, text=f'RE: {message.text}')
app.run()
# try:
#     asyncio.get_event_loop().run_forever()
# except KeyboardInterrupt:
#     log.info('Остановка бота...')
# finally:
#     app.stop()
