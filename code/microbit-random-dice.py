from microbit import *
import random

# A list of all dice images
dice = [Image("00000:"
              "00000:"
              "00900:"
              "00000:"
              "00000"),

        Image("90000:"
              "00000:"
              "00000:"
              "00000:"
              "00009"),

        Image("90000:"
              "00000:"
              "00900:"
              "00000:"
              "00009"),

        Image("90009:"
              "00000:"
              "00000:"
              "00000:"
              "90009"),

        Image("90009:"
              "00000:"
              "00900:"
              "00000:"
              "90009"),

        Image("90009:"
              "00000:"
              "90009:"
              "00000:"
              "90009")]

display.show(Image.HAPPY)

while True:
    if accelerometer.was_gesture('shake'):
        display.show(dice, loop=True, wait=False, delay=100)
        sleep(4000)
        display.show(random.choice(dice))                     
    sleep(10)
