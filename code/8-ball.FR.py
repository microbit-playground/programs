"""
    8-Ball Message Generator
    Copyright (c) 2016 Multiple Authors
    MIT  Licence
"""

from microbit import *
import random

# liste des réponses possibles
responses = [
    "C'est certain",
    "C'est vraiment comme ça",
    "Impossible de prédire maintenant",
    "Concentrez vous et recommencez",
    "N'y comptez pas"
    "Ma réponse est non",
    "Mes sources disent non",
    "Outlook n'est pas terrible",
    "Les carottes sont cuites",
]

while True:
    display.show("8")
    if accelerometer.was_gesture("shake"):
        display.clear()
        sleep(1000)
        
        # 1 choisie un élément au hasard dans la liste.
        # 2 Le convertir en chaine de caractères
        # 3 le faire défiler
        display.scroll(random.choice(answers))
