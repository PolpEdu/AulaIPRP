#Eduardo Nunes
from turtle import *
from threading import Thread

screen = Screen()
screen.setup(950,400)

turtles = [Turtle() for x in range(5)] #criei 5 turtles

for i,t in enumerate(turtles):

    #eu preciso do i para dar um numero a todas as tartarugas que vou usar (5)
    #e mete-las numa posiçao diferente
    t.penup()
    t.goto(-300 + 150 * i, 0)
    turtles[0].color("blue")
    turtles[1].color("yellow")
    turtles[2].color("green")
    turtles[3].color("red")
    turtles[4].color("purple")


def movet1():
    for x in range(4):
        turtles[0].forward(100)
        turtles[0].left(90)

def movet2():
    for x in range(5):
        turtles[1].forward(100)
        turtles[1].left(144)

def movet3():
    for x in range(6):
        turtles[2].forward(100)
        turtles[2].left(60)

def movet4():
    for x in range(3):
        turtles[3].forward(100)
        turtles[3].left(120)

def movet5():
    for x in range(5):
        turtles[4].forward(100)
        turtles[4].left(72)


for turtle in turtles:
    turtle.pendown()

if __name__ =="__main__":
    Thread(target = movet1).start()
    Thread(target=movet2).start()
    Thread(target=movet3).start()
    Thread(target=movet4).start()
    Thread(target=movet5).start()

done()
