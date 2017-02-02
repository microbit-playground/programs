from microbit import *
import random

# Show animation for random time
display.show(Image.ALL_CLOCKS, loop=True, wait=False, delay=100)
sleep(random.randint(500, 5000)) 

# prompt user to press button
display.show(Image.ARROW_E) 
start_time = running_time() # set start time

# wait for button_b to be pressed 
while not button_b.was_pressed(): 
    sleep(20)

# record time taken to press button
end_time = running_time() 

# calculate and scroll reaction time
reaction_time = end_time - start_time  
display.scroll(str(reaction_time)) 

# reset if button a is pressed
display.show(Image.ARROW_W) 
while not button_a.was_pressed(): 
    sleep(20)
reset()