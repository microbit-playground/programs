---
title: "Symetrical Snowflakes"
layout: text-width-sidebar

# Meta description for google and sharing
meta-description:  "Draw a snowflake with a random pattern."

# simple description for TOC
simple-description: "Make a Snowflake"

#############
## Options ##
#############

share: True
comments: True
video: True

###############################
## Program Template Specific ##
###############################

# Stapline beneath the header
strapline: "make a snowflake."

# About Box is on the left of the program page
aboutbox: "Builds a 3x3 image for the display. This is rotated (or mirrored) to fill the whole display."

# Difficulty of program: easy, medium or ninja
cats: medium

date: 2016-12-23T10:20:00Z
---

{% highlight python %}
{% include_relative code/snow-flake.py %}
{% endhighlight %}

This program builds a random 3x3 image for the display. This then rotated 45&deg; 3 times fro each corner of the micro:bit.
