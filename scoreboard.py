from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 20, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.count = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.teleport(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score:{self.count} " f"Highest Score: {self.high_score} ", align=ALIGNMENT, font=FONT)

    def update_high_score(self):
        if self.count > self.high_score:
            self.high_score = self.count
            with open("data.txt", mode = "w") as file:
                file.write(f"{self.high_score}")
        self.count = 0
        self.update_scoreboard()

    def update_count(self):
        self.count += 1
        self.update_scoreboard()