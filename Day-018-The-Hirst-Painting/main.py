import turtle as t
import random

t.colormode(255)    #Allows us to use RGB values in turtle graphics
tim = t.Turtle()
color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123),
              (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70),
              (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129),
              (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

tim.setheading(225)
tim.penup()
tim.hideturtle()    #Hides the turtle cursor so that it doesn't appear in the final painting
tim.speed("fastest")
tim.forward(300)
tim.setheading(0)   #Sets the turtle's heading facing right
number_of_dots = 100

for dot_count in range(1,number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.penup()
    tim.forward(50)
    
    if dot_count % 10 == 0:  # After every 10 dots, move the turtle to the next row
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = t.Screen()
screen.exitonclick()    #Keeps the turtle graphics window open until the user clicks on it
