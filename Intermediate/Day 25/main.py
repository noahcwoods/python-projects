import turtle
import pandas

image = "blank_states_img.gif"

screen = turtle.Screen()
screen.title("US States Game")
screen.setup(width=725, height=491)
screen.addshape(image)
turtle.shape(image)

guessed_states = []
import_data = pandas.read_csv("50_states.csv")
states_data = import_data.state.to_list()
done = False
while not done:

    answer_state = screen.textinput(title=f"Guess the State {len(guessed_states)}/50",
                                    prompt="Enter another state name.")

    if answer_state == "Exit":
        done = True
    if answer_state in states_data:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = import_data[import_data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
    if len(guessed_states) == 50:
        done = True

for state in states_data:
    if state in guessed_states:
        states_data.remove(state)
export_data = pandas.DataFrame(states_data)
export_data.to_csv("states_to_learn")
