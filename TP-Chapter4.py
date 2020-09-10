from swampy.TurtleWorld import *
import math

# Exercies 1-4 - Exercise 4.3
def exercise_1():
    def square(t):
        for _ in range(4):
            fd(t, 200)
            lt(t)

    world = TurtleWorld()
    bob = Turtle()

    square(bob)


def exercise_2():
    def square(t, l):
        for _ in range(4):
            fd(t, l)
            rt(t)

    world = TurtleWorld()
    bob = Turtle()
    length = 200

    square(bob, length)


def exercise_3():
    def polygon(t, l, n):
        for _ in range(n):
            fd(t, l)
            rt(t, 360.0 / n)

    world = TurtleWorld()
    bob = Turtle()
    length = 50

    polygon(bob, length, 8)


def exercise_4():
    def circle(t, r):
        for _ in range(90):
            fd(t, 2 * math.pi * r * (4 / 360))
            rt(t, 360 / 90)
"""
    def circle(t, r): # example code from the book
        circumference = 2 * math.pi * r
        n = int(circumference / 3) + 1
        length = circumference / n
        polygon =(t, n, length)
"""
    world = TurtleWorld()
    bob = Turtle()
    bob.delay = 0.01
    radius = 50

    circle(bob, radius)


def exercise_5():
    def arc(t, r, a):
        for _ in range(a % 360):
            fd(t, 2 * math.pi * r * (1 / 360))
            rt(t, 1)

    world = TurtleWorld()
    bob = Turtle()
    bob.delay = 0.01
    radius = 50
    angle = 180

    arc(bob, radius, angle)


exercise_1()
exercise_2()
exercise_3()
exercise_4()
exercise_5()

