from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for turtle_index in STARTING_POSITIONS:       # Create 3 segments of the snake and position them next to each other
            turtle = Turtle("square")
            turtle.penup()
            turtle.color("white")
            turtle.goto(turtle_index)
            self.segments.append(turtle)
            
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):     # Move each segment to the position of the segment in front of it
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE) # Move the head segment forward by 20 units AND the rest of the segments will follow it because of the above loopself.
        
    def up(self):
        if self.head.heading() != 270: # Prevent the snake from going in the opposite direction
            self.head.setheading(90)
    
    def down(self):
        if self.head.heading() != 90: # Prevent the snake from going in the opposite direction
            self.head.setheading(270)
    
    def left(self):
        if self.head.heading() != 0: # Prevent the snake from going in the opposite direction
            self.head.setheading(180)
    
    def right(self):
        if self.head.heading() != 180: # Prevent the snake from going in the opposite direction
            self.head.setheading(0)