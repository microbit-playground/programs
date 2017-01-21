---
title: "Make an 8-Ball for your micro:bit"
layout: text-width-sidebar

# Meta description for google and sharing
meta-description:  "Python code to turn your micro:bit into an 8-ball."

# simple description for TOC
simple-description: "8-Ball"

#############
## Options ##
#############

share: true
comments: yes

###############################
## Program Template Specific ##
###############################

# Stapline beneath the header
strapline: "`random` to pick an item from a list"

# About Box is on the left of the program page
aboutbox: "Make a funky 8-ball for the microbit. It shows a different message each time it's shaken."

# Difficulty of program: easy, medium or ninja
cats: easy

date:         2016-12-23T10:20:00Z
date-updated: 2016-12-23T10:20:00Z
---

{% highlight python %}
{% include_relative code/8-ball.py %}
{% endhighlight %}

###  Code Explained
{: .ui .dividing .header}

#### answers List

Each of the possible messages is held in a list. A list holds multiple values. In this example, the list has 9 values and each one of those 9 values is a string (of characters).

{% highlight python %}
answers = [
    "It is certain",
    "It is decidedly so",
    "Cannot predict now",
    "Concentrate and ask again",
    "Don't count on it"
    "My reply is no",
    "My sources say no",
    "Outlook not so good",
    "Very doubtful",
{% endhighlight %}


The square brackets and each item is separated by a comma. The list can also be arranged on a single line:

{% highlight python %}

answers = ["It is certain", "Dont count on it", "Ask again",]

{% endhighlight %}


#### Was it Shaken?

{% highlight python %}
if accelerometer.was_gesture("shake") is True:
{% endhighlight %}

`.was_gesture(gesture)` returns a True or False depending on whether `gesture` was the most recently detected gesture. `.was_gesture(freefall)` would return `True` if the microbit was thrown into the air.

The [API for the `accelerometer` module lists other gestures that can be used.](http://microbit-micropython.readthedocs.org/en/latest/accelerometer.html)

#### Random Choice from List

{% highlight python %}
display.scroll(answers.choice)
{% endhighlight %}

`.choice` picks a random item from the `answers` list.

Using `random` requires the `random` module to be imported. This is done at the beginning of the program:

{% highlight python %}
from microbit import *
import random
{% endhighlight %}

A module (like `random`) is a collection of pre-existing code you can reuse.
