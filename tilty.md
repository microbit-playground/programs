---
title: "Tilty Game"
layout: text-width-sidebar

# Meta description for google and sharing
meta-description:  "A game of skill for the micro:bit."

# simple description for TOC
simple-description: "Tilty Game"

#############
## Options ##
#############

share: True
comments: True

###############################
## Program Template Specific ##
###############################

# Stapline beneath the header
strapline: "keep it level"

# About Box is on the lseft of the program page
aboutbox: "Try to keep the microbit level"

# Difficulty of program: easy, medium or ninja
cats: ninja

date:         2016-12-23T10:20:00Z
date-updated: 2016-12-23T10:20:00Z
---

Move the micro:bit through the x- and y axis to illuminate all the squares.

{% highlight python %}
{% include_relative code/tilty.py %}
{% endhighlight %}
