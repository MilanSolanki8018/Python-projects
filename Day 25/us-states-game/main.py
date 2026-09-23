import turtle
from mimetypes import guess_type
from turtle import Turtle,Screen
import pandas

screen = Screen()
screen.title("U.S State Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# datas = csv.reader("50_states.csv")
# for data in datas:
#     print(data)

data = pandas.read_csv("50_states.csv")
print(data)
all_states = data.state.to_list()

guess_states = []

while len(guess_states) < 3:
    answer_state = screen.textinput(title=f"{len(guess_states)}/50 State Correct",prompt="What's another state name?").title()

    if answer_state == "Exit":
        missing_state = [state for state in all_states if state not in guess_states]
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("state.csv")
                # with open("state.csv", mode="a") as states_data:
                #     states_data.write(f"{state}\n")
        break

    if answer_state in all_states:
        s_turtle = Turtle()
        s_turtle.hideturtle()
        s_turtle.penup()
        state_data = data[data.state == answer_state]
        s_turtle.goto(state_data.x.item(),state_data.y.item())
        s_turtle.write(answer_state)
        guess_states.append(answer_state)

#create csv file remaining state name:
