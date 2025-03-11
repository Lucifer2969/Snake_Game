from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 20, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.color("white")
        self.teleport(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f"Score:{self.count}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.teleport(0, 0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)

    def update_count(self):
        self.count += 1
        self.clear()
        self.update_scoreboard()