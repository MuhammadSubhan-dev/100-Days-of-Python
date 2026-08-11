from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1  # Control the speed of the ball's movement
        
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)  # Move the ball to the new position
        
    def bounce_y(self):
        self.y_move *= -1  # Reverse the y-direction of the ball's movement
    
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9  #Increase the speed of the ball after bouncing off a paddle
        
    def reset_position(self):
        self.goto(0, 0)  # Reset the ball's position to the center
        self.move_speed = 0.1  #Reset the speed of the ball
        self.bounce_x()  # Reverse the x-direction of the ball's movement