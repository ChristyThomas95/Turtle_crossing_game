from turtle import Turtle

STARTING_STAGE = (0, -280)
MOVE_DISTANCE = 10
FINISHING_POINT = 280

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.penup()
        self.go_to_starting()


    def go_to_starting(self):
        self.goto(STARTING_STAGE)

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def finishing_point(self):
      if self.ycor() > FINISHING_POINT:
         return True
      else:
         return False

    