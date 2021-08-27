from turtle import Turtle

class Score(Turtle):

    def __init__(self):

        super().__init__()
        self.score = 0
        self.color("black")
        self.penup()
        self.goto(0, 265)
        self.write_score()
        self.hideturtle()

    def write_score(self):
        self.write(f"Score: {self.score}", align="center", font=("Comic Sans", 20, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write_score()

    def game_over(self):
        self.goto(0,0)
        self.color("black")
        self.write("GAME OVER", align="center", font=("Comic Sans", 20, "normal"))

