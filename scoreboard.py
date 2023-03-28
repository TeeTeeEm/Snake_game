from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "bold")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.text = None
        self.penup()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.goto(0, 265)
        self.update_scoreboard()

    def add_point(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.text = f"Score: {self.score}"
        self.write(self.text, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

