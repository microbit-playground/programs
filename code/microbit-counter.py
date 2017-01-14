from microbit import *

count = 0

while True:
    display.show(Image.ARROW_W)
    if button_a.was_pressed():
        count += 1
    elif button_b.was_pressed():
        display.scroll(str(count), delay=100)
    elif button_a.is_pressed() and button_b.is_pressed():
        count = 0
        display.scroll("Reset", delay=100)