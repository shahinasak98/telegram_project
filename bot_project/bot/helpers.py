
import json
import random

def option():
    """Helper function to list out options"""

    options = ['Fat','Dumb', 'Stupid']
    return options

def telegram_keyboard():
    """Helper function to give user with options"""
    keyboard = option()
    keyboard = json.dumps(keyboard)

    return keyboard

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
    if data=="Stupid":
        result_message= random.choice(jokes['Stupid'])
    elif data=="Fat":
        result_message= random.choice(jokes['Fat'])
    elif data=="Dumb":
        result_message= random.choice(jokes['Dumb'])
    else:
        result_message="WRONG CHOICE"
    return result_message