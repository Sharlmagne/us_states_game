from turtle import Turtle
FONT = ("Arial", 8, "normal")


class State(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def placement(self, state, location):
        self.goto(location)
        self.write(state, align="center", font=FONT)