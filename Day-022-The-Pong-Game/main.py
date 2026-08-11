from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.title("Pong Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)  # Turn off automatic screen updates for smoother animation

scoreboard = Scoreboard()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()  # Create the ball object

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")      #Moves the paddle up when the "Up" arrow key is pressed
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")      #Onkeypress event for continously moving the left paddle up when the "w" key is pressed
screen.onkeypress(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    
    time.sleep(ball.move_speed)  # Control the speed of the game loop
    screen.update()  # Update the screen to reflect changes
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:  # Check for collision with top/bottom walls
        ball.bounce_y()
    
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:  # Check for collision with right paddle
        ball.bounce_x()    

    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        
    if ball.xcor() > 380:  # Ball goes past the right paddle
        scoreboard.increase_score_l()
        ball.reset_position()
        
    if ball.xcor() < -380:
        scoreboard.increase_score_r()
        ball.reset_position()
    
screen.exitonclick()