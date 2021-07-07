from turtle import Turtle
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        with open("highscore.txt") as file:
            contents = file.read()
        self.score = 0
        self.highscore = int(contents)
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.write(f"Score: {self.score} Highscore: {self.highscore} ", align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score} Highscore: {self.highscore} ", align="center", font=("Arial", 24, "normal"))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscore.txt", mode="w") as file:
                file.write(str(self.highscore))
        self.score = 0
        self.clear()
        self.write(f"Score: {self.score} Highscore: {self.highscore} ", align="center", font=("Arial", 24, "normal"))
