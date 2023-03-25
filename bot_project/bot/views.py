from django.shortcuts import render
from django.http import HttpResponse
import asyncio
from .consumer import dp
from .helpers import user_count
# Create your views here.

def TelegramView(request):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    # Start the aiogram dispatcher and handlers
    loop.create_task(dp.start_polling())

    # Return a response
    return HttpResponse("Hello, World!")

def TelegramCount(request):
    if request.method == 'GET':
        data = user_count()
        return render(request, 'bot/index.html', {'data': data})
 