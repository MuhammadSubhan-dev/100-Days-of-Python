from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)



segments = []
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

    
screen.update()
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh() # Move the food to a new random position
        scoreboard.increase_score() # Increase the score by 1
        snake.extend() # Add a new segment to the snake at the position of the last segment
        
    #Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()
        
    #Detect collision with tail
    for segment in snake.segments[1:]: # Loop through all the segments of the snake except the head
        if snake.head.distance(segment) < 10: # Check if the head collides with any segment of the snake's body
            scoreboard.reset()
            snake.reset()
            
screen.exitonclick()