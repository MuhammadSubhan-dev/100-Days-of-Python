from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("my_highscores.txt") as file:     #(We dont have to close our files using with method)
            self.highscore = int(file.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.highscore}", align="center", font=("Courier", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
        
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("my_highscores.txt","w") as file:
                file.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()
