from aiogram import Bot, Dispatcher
from django.conf import settings
from channels.generic.websocket import AsyncWebsocketConsumer
from bot.helpers import telegram_keyboard, option, choose_joke
from django.conf import settings

bot = Bot(token=settings.TELEGRAM_TOKEN)
dp = Dispatcher(bot)


class Botconsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.bot_token = settings.TELEGRAM_TOKEN
        self.chat_id = None
        await self.accept()
    
    async def receive(self, text_data):

        # self.chat_id,message = get_response(text_data)
        updates = await bot.get_updates()
        chat_id = updates[-1].message.chat.id
        self.chat_id = chat_id
        if text_data == "/start":
            await bot.send_message(chat_id=self.chat_id,text=telegram_keyboard()
            )
        
        if text_data in option():
            await bot.send_message(chat_id=self.chat_id,text=choose_joke(text_data))

        
        




        
