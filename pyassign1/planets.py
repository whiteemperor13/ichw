#!/usr/bin/env python3

"""planets.py: Using the turtle module to build a model for the oribts of the planets in the solar system

__author__ = "Xiangtao Hu"
__pkuid__  = "1700011768"
__email__  = "white_emperor@pku.edu.cn"
"""

import math
import turtle

def initial():
    """setting the basic parameters, like color, shape, size, etc., for the planets
    """
    for x in range(6):
        wg=eval("wg"+str(x+1))
        color=eval("color"+str(x+1))
        c=eval("c"+str(x+1))
        e=eval("e"+str(x+1))
        wg.speed(0)
        wg.shape("circle")
        wg.turtlesize(0.5,0.5,0.5)
        wg.pensize(1.5)
        wg.color(color)
        wg.penup()
        wg.setx((1/e-1)*c)
        wg.pendown()

def ovalmotion(i):
    """a function that allows 6 planets to move to a point on its oval orbit
    """
    for x in range(6):
        wg=eval("wg"+str(x+1))
        c=eval("c"+str(x+1))
        e=eval("e"+str(x+1))
        n=50*(x+1)
        a=c/e
        b=math.sqrt(a**2-c**2)
        wg.goto(b**2/c*math.cos((i+1)*2*math.pi/n)/(math.cos((i+1)*2*math.pi/n)+a/c),b**2/c*math.sin((i+1)*2*math.pi/n)/(math.cos((i+1)*2*math.pi/n)+a/c))

def solar_system():
    """A function that simulates the orbit of 6 planets in the solar system
    """
    initial()
    for i in range(100000000):
        ovalmotion(i)


def main():
    """main module
    """
    solar_system()

wg=turtle.Screen()
sun=turtle.Turtle()
sun.shape("circle")
sun.turtlesize(1,1,1)
sun.color("yellow")
wg1=turtle.Turtle()
color1="blue"
c1=5
e1=0.2
wg2=turtle.Turtle()
color2="yellow"
c2=20
e2=0.25
wg3=turtle.Turtle()
color3="darkblue"
c3=40
e3=0.3
wg4=turtle.Turtle()
color4="red"
c4=60
e4=0.35
wg5=turtle.Turtle()
color5="green"
c5=80
e5=0.4
wg6=turtle.Turtle()
color6="brown"
c6=100
e6=0.45

if __name__ == '__main__':
    main()