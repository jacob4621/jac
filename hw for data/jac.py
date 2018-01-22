from turtle import *

jac = Turtle()
jac.forward(100)
jac.left(45)
jac.forward(100)

class RaceTurtle:
    def __init__(self, speed,turnDelay,name):
        self.name = name
        self.turt = Turtle()
        self.speed = 20 * ( 1 + (speed/100))
        self.turnDelay = 0 + turnDelay


    def forward(self, distance):
        """moves the turtle forward speed * distance"""

        self.turt.forward(distance * self.speed)


racerone = RaceTurtle ( 0, 0, "racer one")
eugene = RaceTurtle(15, 500, "eugene 'the machine' topps")

while True:
    racerone.forward(1)
    eugene.forward(1)

    if racerone.turt.x > 100:
        print(racerone.name, "wins")
        break
    if eugene.turt.xcor() > 100:
        print(eugene.name, "wins")
        break
