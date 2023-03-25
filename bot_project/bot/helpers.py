from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import random, json
from .models import TelegramOption,TelegramUser

def option():
    """Helper function to list out options"""

    options = {'Fat':0,'Dumb':1, 'Stupid':2}
    return options

def telegram_keyboard():
    """Helper function to give user with options"""

    button1 = InlineKeyboardButton(text="Fat",callback_data=0)
    button2 = InlineKeyboardButton(text="Dumb",callback_data=1)
    button3 = InlineKeyboardButton(text="Stupid",callback_data=2)
    keyboard = InlineKeyboardMarkup().add(button1, button2, button3)
    keyboard_json = json.dumps(keyboard.to_python())
    return keyboard_json

def choose_joke(data):
    """Helper function to randomly choose a joke from"""

    jokes = {
     'Stupid': ["""Yo' Mama is so stupid, she needs a recipe to make ice cubes.""",
                """Yo' Mama is so stupid, she thinks DNA is the National Dyslexics Association."""],
     'Fat':    ["""Yo' Mama is so fat, when she goes to a restaurant, instead of a menu, she gets an estimate.""",
                """ Yo' Mama is so fat, when the cops see her on a street corner, they yell, "Hey you guys, break it up!" """],
     'Dumb':   ["""Yo' Mama is so dumb, when God was giving out brains, she thought they were milkshakes and asked for extra thick.""",
                """Yo' Mama is so dumb, she locked her keys inside her motorcycle."""] 
     }
    if data==str(0):
        result_message= random.choice(jokes['Fat'])
    elif data==str(1):
        result_message= random.choice(jokes['Dumb'])
    elif data==str(2):                                                  
        result_message= random.choice(jokes['Stupid'])
    else:
        result_message="WRONG CHOICE"
    return result_message


def user_count():
    """To get the count of each options selected by user"""

    data = []
    users = TelegramUser.objects.all()
    for user in users:
        option0 = TelegramOption.objects.filter(chat=user.chat_id,choice=0).count()
        option1 = TelegramOption.objects.filter(chat=user.chat_id,choice=1).count()
        option2 = TelegramOption.objects.filter(chat=user.chat_id,choice=2).count()
        content = {'chat_id': user.chat_id, 'option0_count': option0, 'option1_count': option1, 'option2_count': option2}
        data.append(content)
    return data