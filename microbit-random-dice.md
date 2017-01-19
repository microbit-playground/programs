---
title: "A microbit dice to display a random number"
layout: text-width-sidebar

# Meta description for google and sharing
meta-description:  "Python program for the microbit to take a random image from a list and display it on the microbit's display."

# simple description for TOC
simple-description: "Random Dice"

#############
## Options ##
#############

share: true

###############################
## Program Template Specific ##
###############################

# Stapline beneath the header
strapline: "`random` to pick an item from a list"

# About Box is on the left of the program page
aboutbox: "Make a dice to display a random image each time the microbit is shaken."

# Difficulty of program: easy, medium or ninja
cats: easy

date: 2017-01-18T10:20:00Z
---

{% highlight python %}
{% include_relative code/microbit-random-dice.py %}
{% endhighlight %}

This is similar to the [8-Ball example also on the website.](/programs/8-ball)

A list of images is given to the microbit. When it is shaken, the microbit uses `random.choice` to pick an item from the list.

##  Code Explained
{: .ui .dividing .header}

There are two main elements to this script: representing images as strings and picking a random item from a list.

{: .ui .dividing .header}
### Using Images

#### `Image` class

The microbit has the `Image` class which contains many images, such as `Image.HAPPY` and `Image.SAD`. These are simply string representations of the images. We can connect to the microbit over `REPL` and see these strings:

{% highlight python %}
>>> print(Image.HAPPY)
Image(
    '00000:'
    '09090:'
    '00000:'
    '90009:'
    '09990:'
)
>>>
{% endhighlight %}

`0` is off whereas `9` is the LED lit at full intensity.

#### Making Custom Images

It is possible for use to then draw our own images on the display. Here `add_sign` variable is a representation of an addition sign.

{% highlight python %}
add_sign = Image("00900:"
                 "00900:"
                 "99999:"
                 "00900:"
                 "00900")
{% endhighlight %}

#### Formatting Image Strings
There are many ways of representing this string. With a colon (as above) or with a new line (`\n`):

{% highlight python %}
add_sign = Image("00900\n"
                 "00900\n"
                 "99999\n"
                 "00900\n"
                 "00900")
{% endhighlight %}

It is also possible to keep the image representation all on one line:

{% highlight python %}
Image("00900:00900:99999:00900:00900")
{% endhighlight %}

#### Lists of Images
In this program, all six dice faces are in a list called `dice`. There are six items in the list in total.

The list begins and ends with a `[ ]` square brackets. Each item in the list is separated with a comma.

{% highlight python %}
dice = [
        Image("00000:00000:00900:00000:00000"), # 1
        Image("90000:00000:00000:00000:00009"), # 2
        Image("90000:00000:00900:00000:00009"), # 3
        Image("90009:00000:00000:00000:90009"), # 4
        Image("90009:00000:00900:00000:90009"), # 5
        Image("90009:00000:90009:00000:90009")  # 6
        ]
{% endhighlight %}

This is exactly the same as the main example above except the image strings are all on one line.

{: .ui .dividing .header}
### Logic

#### Was it Shaken?

{% highlight python %}
if accelerometer.was_gesture("shake") is True:
{% endhighlight %}

`.was_gesture(gesture_name)` returns `True` or `False` if `gesture_name` was the most recently detected gesture. `.was_gesture("shake")` returns True if it was shaken.

#### Pick Random Item

The `dice` list has 6 items. `random.choice` is used on the list to return a random item:

{% highlight python %}
display.show(random.choice(dice))
{% endhighlight %}

Using `random` requires the `random` module to be imported. This is done at the beginning of the program:

{% highlight python %}
from microbit import *
import random
{% endhighlight %}
