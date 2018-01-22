import turtle
import time

jac = Turtle()
jac.forward(100)
jac.left(45)
jac.forward(100)

class RaceTurtle:
    def __init__(self, speed,turnDelay,name):
        self.name = name
        self.turt = turtle.Turtle()
        self.speed = speed
        self.turnDelay = 0 + turnDelay

    def getX(self):
        return self.turt.xcor()

    def getY(self):
        return self.turt.ycor()
    
    def forward(self, distance):
        self.turt.forward(1)

    def

    def runRace( rt ):
        time.clock()
        startTime = time.clock()
        leg1distance = 100 * (1 - rt.speed/100)

        for i in range(leg1distance):
            rt.forward()

racerone = RaceTurtle ( 0, 0, "racer one")
eugene = RaceTurtle(15, 500, "eugene 'the machine' topps")

eugene.turt.penup()
eugene.turt.sety( 150)
eugene.turt.pendown()

#while True:
    #racerone.forward(1)
    #eugene.forward(1)

   # if racerone.turt.x > 100:
        #print(racerone.name, "wins")
       # break
   # if eugene.turt.xcor() > 100:
        #print(eugene.name, "wins")
       # break
