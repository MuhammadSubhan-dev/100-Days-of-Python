from turtle import Turtle, Screen
import random

screen = Screen()

screen.setup(width=500, height=400)
screen.title("Turtle Racing Game")
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "blue", "green", "yellow", "orange", "purple"]
all_turtles = []

is_race_on = False

for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-100 + turtle_index * 40)     #X position remains same for all the turtles,
                                                            #Y position is calculated based on the index to space out the turtles vertically.
    all_turtles.append(new_turtle)
        
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
                turtle.write(f"🎉 You win! {winning_color} wins!", align="center", font=("Arial", 24, "bold"))
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
                turtle.write(f"😢 You lose! {winning_color} wins!", align="center", font=("Arial", 24, "bold"))
            is_race_on = False
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()