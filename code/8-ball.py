"""
    8-Ball Message Generator
    Copyright (c) 2016 Multiple Authors
    MIT  Licence
"""

from microbit import *
import random

# list of possible answers
answers = [
    "It is certain",
    "It is decidedly so",
    "Cannot predict now",
    "Concentrate and ask again",
    "Don't count on it",
    "My reply is no",
    "My sources say no",
    "Outlook not so good"
    "Very doubtful",
]

while True:
    display.show("8")
    if accelerometer.was_gesture("shake"):
        display.clear()
        sleep(1000)
        
        # 1 pick a random item from the list. 
        # 2 Convert it to a string
        # 3 scroll it.
        display.scroll(random.choice(answers))
