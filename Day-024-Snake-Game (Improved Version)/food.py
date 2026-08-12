from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5) # Make the food smaller
        self.color("blue")
        self.speed("fastest")
        random_x = random.randint(-280, 280) # Random x position for the food
        random_y = random.randint(-280, 280) # Random y position for the food
        self.goto(random_x, random_y) # Move the food to the random position
        self.refresh() # Call the refresh method to move the food to a new random position
        
        
    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)