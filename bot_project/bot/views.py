from django.shortcuts import render
from django.http import HttpResponse
import asyncio
from .consumer import dp
# Create your views here.

def my_view(request):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    # Start the aiogram dispatcher and handlers
    loop.create_task(dp.start_polling())

    # Return a response
    return HttpResponse("Hello, World!")
 