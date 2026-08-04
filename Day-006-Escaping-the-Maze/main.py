#Maze Escaper reference taken from Reeborg's World (Maze)
def turn_right():
    turn_left()
    turn_left()
    turn_left()

#Easy Solution
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
        
#Hard Solution
while front_is_clear():
    move()
turn_left()     #After this while the robot will probably reach location where there is a wall on right
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()