from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)  # Make the paddle taller
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20  # Move the paddle up by 20 units
        self.sety(new_y)

    def go_down(self):
        new_y = self.ycor() - 20  # Move the paddle down by 20 units
        self.sety(new_y)