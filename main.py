import pandas as pd
import turtle
from state import State

screen = turtle.Screen()
screen.title("U.S States Game")
img = "blank_states_img.gif"
screen.addshape(img)
screen.setup(width=750, height=500)
turtle.shape(img)

df = pd.read_csv("50_states.csv")
state = State()

states_to_learn = df["state"].tolist()
end_of_game = False
correct_ans = 0
while not end_of_game:
    if correct_ans == 0:
        ans = screen.textinput(title="Guess the State", prompt="What's another State's name?").title()
    else:
        ans = screen.textinput(title=f"{correct_ans}/50 States correct", prompt="What's another State's name?").title()

    for state_name in states_to_learn:
        if ans == state_name:
            x = int(df[df["state"] == ans]["x"])
            y = int(df[df["state"] == ans]["y"])
            location = (x, y)
            state.placement(state_name, location)
            states_to_learn.remove(state_name)
            correct_ans += 1
    if correct_ans == 50 or ans == "Exit":
        end_of_game = True
        states_to_learn = pd.DataFrame(states_to_learn, columns=["States to Learn"])
        states_to_learn.to_csv("states_to_learn.csv", index=False)

screen.exitonclick()