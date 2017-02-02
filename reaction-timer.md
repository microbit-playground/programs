---
title: "Reaction Timer"
layout: text-width-sidebar

# Meta description for google and sharing
meta-description:  "microbit game in python to time the reaction speed of a user pressing a button."

# simple description for TOC
simple-description: "Reaction Timer"

#############
## Options ##
#############

share: true
comments: yes
author: romilly

###############################
## Program Template Specific ##
###############################

# Stapline beneath the header
strapline: "Reaction Timer Game"

# About Box is on the left of the program page
aboutbox: "A single person game to time the reaction speed of a user's input."

# Difficulty of program: easy, medium or ninja
cats: medium

date:         2017-02-02T10:20:00Z
date-updated: 2017-02-02T10:20:00Z
---  

{% highlight python %}{% include_relative code/reaction-timer.py %}{% endhighlight %}

This is a simple game to show how long it takes a user to press a button. 

* Show an animation of a clock face for a random amount of time
* Prompt user to press a button
* Display time taken for the user to press the button

A video will go here.

### Code Explained
{: .ui .dividing .header}



#### Import Random
{% highlight python %}
from microbit import *
import random
{% endhighlight %}

The program uses `random.randint(500, 5000)` to return a random number between 500 and 5000. The random number module must be imported with `import random`. 

The random number between `500` and `5000` is used to tell the microbit to sleep for a random amount of time between .5 and 5 seconds.



#### Clock Animation
A clock animation is shown on the microbit before prompting the user to press a button. The code is:

{% highlight python %}
display.show(Image.ALL_CLOCKS, loop=True, wait=False, delay=100)
{% endhighlight %}

`Image.ALL_CLOCKS` is a list of all the clock images, eg `CLOCK1`, `CLOCK2`, `CLOCK3`, etc. 

The [microbit micropython documentation gives a complete explaination](http://microbit-micropython.readthedocs.io/en/latest/display.html) of `display.show`: 

In this program, `loop=True` causes all images in the `Image.ALL_CLOCKS` list to repeat. `wait=False` causes the animation to happen the the background.



#### Calculate Reaction Time
* `running_time()` returns the amount of time the microbit has been running in milliseconds since the last reset.
* `start_time` is the time at which the timer began waiting for a user to press button_b.
* `end_time` is the time at which the user pressed button_b. 

The difference between `start_time` and `end_time` is the time in milliseconds it took for the user to press button_b.



#### Wait for User to Press Button
{% highlight python %}
while not button_b.was_pressed():
    sleep(20)
{% endhighlight %}

`button_b.was_pressed()` returns true if `button_b` was pressed since the last time it was called. 

This `while loop` continues while button_b was not pressed. It essentially waits for `button_b` to be pressed.



#### Scroll Reaction Time

{% highlight python %}
display.scroll(str(reaction_time))
{% endhighlight %}

Convert `reaction_time` (the time taken for the user to press the button) to a string and scroll it on the display.



#### Reset 

{% highlight python %}
display.show(Image.ARROW_W) 
while not button_a.was_pressed():
    sleep(20)
reset()
{% endhighlight %}

At the end of the program, an arrow points at `button_a`. A `while` loop waits for the user to press `button_a`.

When `button_a.was_pressed()`, `reset()` is called which restarts the microbit and causes the program to run again. 



### Next Steps

* It's possible to cheat but pressing `button_b` when the clock animation is showing. Introduce a way of stopping the cheating.
* Make a two player game.



### See More

* This program is also [written up here](http://blog.rareschool.com/2017/01/a-simple-reaction-timer-in-micropython.html).
* The code is available [on github](https://github.com/microbit-and-chips/reaction-timer).