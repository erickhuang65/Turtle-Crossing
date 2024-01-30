from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = "left"
FONT = "normal"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.hideturtle()
        self.goto(-250, 250)
        self.color("black")
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_level()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)