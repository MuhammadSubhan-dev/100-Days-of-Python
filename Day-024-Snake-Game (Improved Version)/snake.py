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
            self.add_segment(turtle_index)
            
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
    
    def add_segment(self,position):
        segment = Turtle("square")
        segment.penup()
        segment.color("white")
        segment.goto(position)
        self.segments.append(segment)
        
    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)     #Moves the previous snakes out of screen
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
            
    def extend(self):
        self.add_segment(self.segments[-1].position()) # Add a new segment to the snake at the position of the last segment