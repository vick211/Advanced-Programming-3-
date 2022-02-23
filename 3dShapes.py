#completely at a loss on this assignment, I tried everything and couldnt get a working something, sorry

from vpython import *

import random
import time

#decides and creates outside shape
def shape1(n):
    shapes
    if n == 1:
        length =3
        width =3
        height =3
        box1 =box(color=color.blue,
            opacity=0.5,
            pos = vector(0,0,0),
            length = length,
            width = width,
            height =height)
        return box1, length, width,height
    if n == 2:
        radius = 10
        sphere1 =sphere(color=color.cyan,
               opacity = 0.5,
               pos = vector(0,0,0),
               radius=radius)
        return sphere1

    if n == 3:
        size1 = vector(10,4,4)
        pyramid1=pyramid(color=color.green,
                opacity = 0.5,
                pos= vector(0,0,0),
                size= size1)
        return pyramid1, size1
    else:
        return 0
#decides and creates inner shape
def shape2(n):
    length =1
    width=1
    height =.5
    if n == 1:
        box2 =box(color=color.red,
            pos =vector(0,0,0),
            length=length,
            width=width,
            height=height)
        return box2, length, width,height
    if n == 2:
        radius =1
        sphere1 =sphere(color=color.red,
               pos = vector(0,0,0),
               radius = radius)
        return sphere1, radius

    if n == 3:
        size = vector(5,2,2)
        pyramid1 =pyramid(color=color.purple,
                pos= vector(0,0,0),
                size= size)
        return pyramid1,size
    else:
        return 0
# will take measurements of shapes to decide boundaries for points
def createPoints():
    randx = random.randint(-2, 2)
    randy = random.randint(-2, 2)
    randz = random.randint(-2, 2)

    for i in range (50):
        points(pos=[vector(randx,randy,randz)], radius =10, color=color.yellow)
#finds created points and returns their locations
def findPoints():
    return 0


#finds the area of shape1 using measurements
def area():
    return 0

#guesses the area of shape2 based on points
def areaGuess():
    return 0

#runs functions
shape1(1)
shape2(2)
createPoints()