from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

with open("data.txt") as FILE:
    content = int(FILE.read())


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.highest_score = content
        self.score = 0
        self.display()

    def display(self):

        self.color("white")
        self.penup()
        self.goto(0, 270)

        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.highest_score}", move=False, align=ALIGNMENT,
                   font=FONT)

   # def game_over(self):
    #    self.goto(0, 0)
    #    self.write(arg=f"GAME OVER", move=False, align=ALIGNMENT,
    #               font=FONT)

    def reset(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            file = open("data.txt", mode="w")
            file.write(f"{self.highest_score}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
