---
title: "Press the Button"
layout: text-width-sidebar

# Meta description for google and sharing
meta-description:  "How to use buttons and if conditions on the micro:bit in Python."

# simple description for TOC
simple-description: "Microbit Buttons"

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
strapline: "Use the buttons to make a message"

# About Box is on the left of the program page
aboutbox: "Using the buttons on the front of the microbit to display a message"

# Difficulty of program: easy, medium or ninja
cats: medium

date:         2016-12-23T10:20:00Z
date-updated: 2016-12-23T10:20:00Z
---

{% highlight python %}
{% include_relative code/press-the-button.py %}
{% endhighlight %}

### Going Further
{: .ui .dividing .header}

The micro:bit api lists other images that can be drawn on the display. The `Image` class predefined images which can be used with `display.show()`:

`display.show(Image.HAPPY)`

* Image.HEART
* Image.HEART_SMALL
* Image.HAPPY
* Image.SILLY


There is a [full list on the API](http://microbit-micropython.readthedocs.org/en/latest/image.html). Or use the `display` [module](http://microbit-micropython.readthedocs.org/en/latest/display.html) and display a picture.
