---
title: "microbit Sorting Hat for Python"
layout: text-width-sidebar

# Meta description for google and sharing
meta-description:  "Python code to make a Harry Potter sorting hat for the microbit."

# simple description for TOC
simple-description: "Sorting Hat"

#############
## Options ##
#############

share: True
comments: True
author: jez

###############################
## Program Template Specific ##
###############################

# Stapline beneath the header
strapline: "`random` to pick an item from a list"

# About Box is on the left of the program page
aboutbox: "Pick a random item from a list when the microbit button is pressed."

# Difficulty of program: easy, medium or ninja
cats: easy

date:         2016-12-23T10:20:00Z
date-updated: 2016-12-23T10:20:00Z
---

{% highlight python %}
{% include_relative code/sorting-hat.py %}
{% endhighlight %}


### How it Works

#### Create a List of Hogwarts Houses

The names are loaded into a list. In the example above the list is created over 5 lines making it easier to read. A list can be created on one line too:

{% highlight python %}
HOUSES   = ["Gryffindor", "Slytherin", "Ravenclaw", "Hufflepuff",]
{% endhighlight %}

A list contains "objects" (the Python way to say "whatsists", "thingamabobs" or "doodahs"). An object can be any type of thing. In this example the objects are _strings_ (of characters) so the value is surrounded by quotation marks like this: `"`Gryffindor`"`.

#### random.choice(HOUSES)

When `button_a` is pressed, the micro:bit's display scrolls a random house (or in code: `display.scroll(random.choice(HOUSES))`). It uses the `random.choice` method to randomly choose an object in the `HOUSES` list. How simple is that?

`random.choice` requires the `random` module. This is not included by defaults so we need to import it:

{% highlight python %}
import microbit from *
import random
{% endhighlight %}


{% include box.html content="what-to-import" %}



### What is `sleep(100)`?

`while True:` puts the micro:bit into an infinite loop. This means the micro:bit repeats the program's loop as fast as it can. The program runs so fast that the processor cannot keep up and the micro:bit crashes.

`sleep(100)` makes the processor do nothing for 100 milliseconds (or .1 of a second). This slows down the program so the processor can keep up. The processor in your micro:bit is so fast that `microbit.sleep(1)` is enough of a wait.

Computer or phone crashes are often caused by badly written code that creates an infinite loop!
