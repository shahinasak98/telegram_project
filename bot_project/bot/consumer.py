import json
from django.conf import settings
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from bot.helpers import get_response, telegram_keyboard, option, choose_joke

class Botconsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.bot_token = settings.TELEGRAM_TOKEN
        self.chat_id = None
        await self.accept()

    async def receive(self, text_data):

        # self.chat_id,message = get_response(text_data)
        if text_data == "/start":
            await self.send(text_data=telegram_keyboard()
            )
        
        if text_data in option():
            await self.send(text_data=choose_joke(text_data))
        
        




        
