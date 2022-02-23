
import turtle
import random


def triangle(x,y):

    turtle.setheading(0)

    turtle.speed(1)

    turtle.goto(0,0)

    turtle.down()
    turtle.color('black')


    coord1 = random.randint(-200, 200)
    coord2 = random.randint(-200, 200)
    coord3 = random.randint(-200, 200)
    coord3 = random.randint(-200, 200)
    coord4 = random.randint(-200, 200)
    randAngle= random.randint(1,360)

    bisect1 = randAngle /2      #couldnt get my bisecting lines working
    bisect2 = randAngle /2
    bisect3 = randAngle/2

    
    turtle.goto(coord1, coord2)
    turtle.left(randAngle)
    turtle.goto(coord3, coord4)


    turtle.goto(0,0)
    turtle.up()
    turtle.goto(coord1, coord2)
    turtle.down()
    turtle.color('blue')
    turtle.right(bisect1)
    turtle.forward(200)

    turtle.up()
    turtle.goto(coord3, coord4)
    turtle.down()
    turtle.color('blue')
    turtle.right(bisect2)
    turtle.forward(200)

    turtle.up()
    turtle.goto(0, 0)
    turtle.down()
    turtle.color('blue')
    turtle.right(bisect3)
    turtle.forward(200)

    turtle.up()

    turtle.clear()

turtle.onscreenclick(triangle)
