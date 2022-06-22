import pandas
from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()
screen.tracer(0)
turtle.penup()
screen.setup(width=725, height=491)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()
x_coordinates = data["x"].to_list()
y_coordinates = data["y"].to_list()

guessed_states = []

while len(guessed_states) < 50:
    screen.update()
    answer = screen.textinput(title=f"{len(guessed_states)}/50 states", prompt="Can you guess all 50 states?")
    if answer.title() == "Exit":
        break
    for state in states:
        if state == answer.title():
            guessed_states.append(state)
            t = Turtle()
            t.penup()
            t.hideturtle()
            x = data[data["state"] == state]["x"]
            y = data[data["state"] == state]["y"]
            t.goto(int(x.to_string(index=False)), int(y.to_string(index=False)))
            t.write(arg=state, move=False, font=('arial', 8, 'normal'))

not_guessed_states = [state for state in states if state not in guessed_states]

not_guessed_statescv = pandas.DataFrame(not_guessed_states)
not_guessed_statescv.to_csv("not_guessed_statescv")



