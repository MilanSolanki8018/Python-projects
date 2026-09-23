from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def set_new_level(self):
        self.goto(STARTING_POSITION)

    def is_it_finish_level(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def turtle_move(self):
        self.forward(MOVE_DISTANCE)