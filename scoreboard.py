from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "bold")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.goto(0, 265)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                content = str(self.high_score)
                file.write(content)
        self.score = 0
        self.update_scoreboard()

    def add_point(self):
        self.score += 1
        self.update_scoreboard()
