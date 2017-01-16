"""
    Snowflakes

    Copyright (c) 2016 Eleni Lixourioti

    APACHE 2.0 License

"""

from microbit import *
import random

SIDE_SIZE = 3

BRIGHTNESS = {
    0: 0,
    1: 4,
    2: 9,
}


def get_random_corner():
    return [[random.randrange(3) for _ in range(SIDE_SIZE)] for _ in range(SIDE_SIZE)]

def get_flake():
    flake = list(get_random_corner())

    for row in flake:
        row += reversed(row[:-1])  # Middle column doesn't change

    for row in reversed(flake[:-1]):
        flake.append(row)

    return flake


def to_display(flake):
    for y, row in enumerate(flake):
        for x, col in enumerate(row):
            display.set_pixel(x, y, BRIGHTNESS[col])


while True:
    flake = get_flake()
    to_display(flake)
    sleep(1000)
