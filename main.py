import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Games")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


guessed = 0
correct_guesses = []
states_data = pandas.read_csv("50_states.csv")
states = states_data["state"].to_list()

while len(correct_guesses) < 50:
    answer_state = screen.textinput(title=f"{guessed}/50 states guessed", prompt="Name another State.").title()
    if answer_state == "Exit":
        missing_states = [state for state in states if state not in correct_guesses]
#         missing_states = []
#         for state in states:
#             if state not in correct_guesses:
#                 missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in states and answer_state not in correct_guesses:
        print("its in")
        row = states_data[states_data["state"] == answer_state]
        scribble = turtle.Turtle()
        scribble.hideturtle()
        scribble.penup()
        scribble.goto(int(row.x), int(row.y))
        scribble.write(arg=f"{answer_state}", align="center",)
        print(row)
        correct_guesses.append(answer_state)
        print(correct_guesses)
        guessed += 1

turtle.mainloop()
