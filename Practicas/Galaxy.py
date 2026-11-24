import turtle as t
import colorsys
import math as m
import random as r

r.seed(7)
TILT = 0.45

screen = t.Screen()
screen.setup(700, 480)
screen.bgcolor("#03030b")
screen.colormode(1.0)

t.hideturtle()
t.speed(50)
t.penup()

def glow(h, v=1.0):
    return colorsys.hsv_to_rgb(h % 1, 0.7, v)

def place(x, y):
    y *= 0.55
    c, s = m.cos(TILT), m.sin(TILT)
    t.goto(x * c - y * s, x * s + y * c)

def stars():
    for _ in range(140):
        x = r.randint(-385, 385)
        y = r.randint(-285, 285)
        t.goto(x, y)
        t.dot(r.randint(1, 3), "white")

def dust():
    for _ in range(700):
        z = r.gauss(0, 120)
        a = r.uniform(0, 6.283)
        place(z * m.cos(a), z * m.sin(a))
        t.dot(r.randint(2, 4), glow(0.7, 0.3))

def arms(count):
    for i in range(count):
        for k in range(4):
            d = i / count
            a = k * m.pi / 2 + d * 5.5
            z = 10 + d * 290
            s = 4 + d * 26
            x = z * m.cos(a) + r.gauss(0, s)
            y = z * m .sin(a) + r.gauss(0, s)
            place(x, y)
            hue = 0.13 - d * 0.55
            v = r.uniform(0.6, 1)
            size = r.randint(2, 4)
            t.dot(size, glow(hue, v))

def core():
    for _ in range(260):
        z = r.gauss(0, 26)
        a = r.uniform(0, 6.283)
        place(z * m.cos(a), z * m.sin(a))
        t.dot(r.randint(2, 5), glow(0.12))

def sparkle():
    for _ in range(40):
        z = r.gauss(0, 150)
        a = r.uniform(0, 6.283)
        place(z * m.cos(a), z * m.sin(a))
        t.dot(r.randint(5, 8), "white")

stars()
dust()
arms(900)
core()
sparkle()
t.goto(0, 0)
t.dot(26, "#fff3c4")
t.done()