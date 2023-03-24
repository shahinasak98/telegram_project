from aiogram import Bot, Dispatcher,types
from asgiref.sync import sync_to_async
from django.conf import settings
from channels.generic.websocket import AsyncWebsocketConsumer
from bot.helpers import telegram_keyboard, option, choose_joke
from django.conf import settings
from aiogram.utils import executor
from .models import TelegramUser,TelegramOption

bot = Bot(token=settings.TELEGRAM_TOKEN)
dp = Dispatcher(bot)


class Botconsumer(AsyncWebsocketConsumer):
    async def connect():
        await bot.send_message(chat_id=settings.ADMIN_CHAT_ID, text="Bot started")

    @dp.message_handler(content_types=types.ContentType.TEXT)
    async def handle_text_message(message: types.Message):
        chat_id = message.chat.id
        username = message.from_user.full_name
        if message.text == "/start":
            await bot.send_message(chat_id=chat_id, text=telegram_keyboard())
        elif message.text in option():
            choice = option()[message.text]
            chat = await sync_to_async(TelegramUser.objects.filter)(chat_id=chat_id)
            if not await sync_to_async(chat.exists)():
                await sync_to_async(TelegramUser.objects.create)(chat_id=chat_id, user=username)
            chat = await sync_to_async(TelegramUser.objects.get)(chat_id=chat_id)
            await sync_to_async(TelegramOption.objects.create)(choice=choice, chat=chat)
            await bot.send_message(chat_id=chat_id,text=choose_joke(message.text))
        else:
            await bot.send_message(chat_id=chat_id,text=f"Thanks for texting {username}, Shahina will let you know what to do. Give a /start message for options of Jokes.Select any from them :).")

        
        

executor.start_polling(dp, skip_updates=True)


        
