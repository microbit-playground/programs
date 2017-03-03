---
title: "Fabriquez une 8-Ball pour votre micro:bit"
layout: text-width-sidebar

# Meta description for google and sharing
meta-description:  "Code Python pour transformer votre micro:bit en 8-ball."

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
strapline: "`random` pour choisir un élément dans une liste"

# About Box is on the left of the program page
aboutbox: "Fabriquez une 8-Ball bien funky pour votre micro:bit. A message différent apparait à chaque fois que vous secouez la carte."

# Difficulty of program: easy, medium or ninja
cats: easy

date:         2017-03-03T18:00:00Z
date-updated: 2017-03-03T18:00:00Z
---

{% highlight python %}
{% include_relative code/8-ball.FR.py %}
{% endhighlight %}

###  Explication du code
{: .ui .dividing .header}

#### Liste de réponses

Chacun des messages possibles est stocké dans une liste. Une liste contient plusieurs valeurs. Dans cet exemple, la liste a 9 valeurs et chacune de ces 9 valeurs est une chaîne de caractères.

{% highlight python %}
responses = [
    "C'est certain",
    "C'est vraiment comme ça",
    "Impossible de prédire maintenant",
    "Concentrez vous et recommencez",
    "N'y comptez pas"
    "Ma réponse est non",
    "Mes sources disent non",
    "Outlook n'est pas terrible",
    "Les carottes sont cuites",
{% endhighlight %}


Entre les crochets, les éléments sont séparés par des virgules La liste peut également être écrite en une seule ligne.

{% highlight python %}

reponses = ["C'est certain", "N'y comptez pas", "Les carottes sont cuites",]

{% endhighlight %}


#### La carte a été secouée ?

{% highlight python %}
if accelerometer.was_gesture("shake") is True:
{% endhighlight %}

`.was_gesture(gesture)` retourne la valeur True ou False en fonction du fait que `gesture` était le dernier geste détecté. `.was_gesture(freefall)` retournerait `True` si la microbit était lancée dans les airs.

L'[API du module `accelerometer` liste d'autres gestes qui sont utilisables.](http://microbit-micropython.readthedocs.org/en/latest/accelerometer.html)

#### Choix aléatoire dans la liste

{% highlight python %}
display.scroll(answers.choice)
{% endhighlight %}

`.choice` choisi un élément au hasard dans la liste `reponses`.

Pour pouvoir utiliser `random` il faut que le module `random` soit importé. Cela est fait au début du programme :

{% highlight python %}
from microbit import *
import random
{% endhighlight %}

Un module (comme `random`) est une collection de code pré-existant que vous pouvez réutiliser.
