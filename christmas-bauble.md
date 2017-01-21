---
title: "Scrolling Bauble"
layout: text-width-sidebar

# Meta description for google and sharing
meta-description:  "Python program to create a scrolling bauble on the BBC Microbit."

# simple description for TOC
simple-description: "Christmas Bauble"

#############
## Options ##
#############

share: true
comments: yes
author: jez
video: true

###############################
## Program Template Specific ##
###############################

# Stapline beneath the header
strapline: "Scroll text on the microbit display"

# About Box is on the left of the program page
aboutbox: "Make a simple Christmas bauble to scroll a festive message across the display."

# Difficulty of program: easy, medium or ninja
cats: easy

date:         2016-12-23T10:20:00Z
date-updated: 2016-12-23T10:20:00Z
---  

{% highlight python %} {% include_relative code/christmas-bauble.py %} {% endhighlight %}


### Code Explained
{: .ui .dividing .header}

`from microbit import *`

This imports the microbit module into the program. `*` imports _everything_ in the module.

Since we only use the `display` module, we could use `from microbit import display`.

`display.scroll("ho ho ho")`

Scrolls the text across the micro:bit's display. Everything inside the `"` is shown in the display. Characters within `"` are strings.

### Reading the API
{: .ui .dividing .header}


[The microbit API for the display module](http://microbit-micropython.readthedocs.org/en/latest/display.html) describes a `delay` parameter for the `scroll` method.

`display.scroll("ho ho ho", delay=500)` updates the display every 500 milliseconds (or half a second). It slows down the speed of the scrolling text.

The API documentation has information that microbit module. Try reading it when you're coding for ideas.  The Python community are also famously helpful - search online for mailing lists and message boards that may contain the help you need. If in doubt, ask for help.

### Going Further
{: .ui .dividing .header}

This only scrolls the message once. Read the API to make it repeat.

{% include box.html content="strings-integers" %}
