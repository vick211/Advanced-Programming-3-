#couldnt figure out how to find points in a certain area




import random
import turtle
import time


def shape1(n):
    if n == 1:
        square()
    if n == 2:
        circle()
    if n == 3:
        triangle()
    else:
        return 0

def shape2(n):
    if n == 1:
        square2()
    if n == 2:
        circle2()
    if n == 3:
        triangle2()
    else:
        return 0

def createPoint(randomForward):
    t = turtle.Turtle()
    amountOfPoints = 50
    for x in range(amountOfPoints):
        randomPoint1 = random.randint(0, randomForward)
        randomPoint2 = random.randint(0, randomForward)
        t.penup()
        t.goto(randomPoint1, randomPoint2)
        t.dot()

def createPointCircle(r):
    t = turtle.Turtle()
    amountOfPoints = 50
    for x in range(amountOfPoints):
        randomPoint1 = random.randint(-r, r)
        randomPoint2 = random.randint(0, r)
        t.penup()
        t.goto(randomPoint1, randomPoint2)
        t.dot()
#  def findPoints():
#      randomForward =
#      t = turtle.Turtle()
#      hits = 0
#
#      if turtle.pos >= randomForward
#          hits +=1
#
#          return hits
#
# def guessArea(hits, amountOfPoints, area):
#     precentageOfHits = hits / amountOfPoints
#     guess = area * precentageOfHits
#
#     return guess

def square():
    t = turtle.Turtle()
    randomForward = random.randint(200, 300)
    area = randomForward * randomForward
    for i in range(4):
        t.forward(randomForward)  # Forward turtle by 100 units
        t.left(90)  # Turn turtle by 90 degree
    createPoint(randomForward)
    print("Known area = ", area)


def circle():
    t = turtle.Turtle()
    r = random.randint(150, 200)
    area = 3.14 * (r * r)
    t.circle(r)

    createPointCircle(r)
    print ("Known area = ", area)


def triangle():

    t = turtle.Turtle()
    t.penup()
    t.goto(-100, 0)
    t.pendown()
    randomForward = random.randint(300, 400)
    area = (1/2) *randomForward * randomForward
    t.forward(randomForward)
    for i in range(2):
        t.left(120)
        t.forward(randomForward)

    createPoint(randomForward)
    print("Known area = ", area)


def square2():
    t = turtle.Turtle()
    randomForward = random.randint(49, 200)
    area = randomForward * randomForward
    for i in range(4):
        t.forward(randomForward)  # Forward turtle by 100 units
        t.left(90)  # Turn turtle by 90 degree


def circle2():
    t = turtle.Turtle()
    t.penup()
    t.goto(100, 0)
    t.pendown()
    r = random.randint(49, 100)
    area = 3.14 * (r * r)
    t.circle(r)


def triangle2():
    t = turtle.Turtle()

    randomForward = random.randint(49, 200)
    area = (1 / 2) * randomForward * randomForward
    t.forward(randomForward)
    for i in range(2):
        t.left(120)
        t.forward(randomForward)


shape2(1)
shape1(1)
time.sleep(5)
#findPoints()
#guessArea(hits,amountOfPoints, area )