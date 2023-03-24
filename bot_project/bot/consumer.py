from aiogram import Bot, Dispatcher,types
from django.conf import settings
from channels.generic.websocket import AsyncWebsocketConsumer
from bot.helpers import telegram_keyboard, option, choose_joke
from django.conf import settings
from aiogram.utils import executor


bot = Bot(token=settings.TELEGRAM_TOKEN)
dp = Dispatcher(bot)


class Botconsumer(AsyncWebsocketConsumer):
    async def connect():
        await bot.send_message(chat_id=settings.ADMIN_CHAT_ID, text="Bot started")

    @dp.message_handler(content_types=types.ContentType.TEXT)
    async def handle_text_message(message: types.Message):
        chat_id = message.chat.id
        if message.text == "/start":
            await bot.send_message(chat_id=chat_id, text=telegram_keyboard())
        if message.text in option():
            await bot.send_message(chat_id=chat_id,text=choose_joke(message.text))
        
        

executor.start_polling(dp, skip_updates=True)


        
