import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("State Guesser")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Reading state csv file
states = pd.read_csv("50_states.csv")
state_names = states.state.to_list()

# Check user input
answer_state = screen.textinput(title="Guess A State", prompt="State name?").title()

# List for correctly guessed states
correct_states = []

# Pointer object
pointer = turtle.Turtle()
pointer.hideturtle()
pointer.penup()

# Main loop stays running until the entire list is completed or the game is exited
while len(correct_states) < len(state_names):


    # Exit condition
    if answer_state is None or answer_state.lower() == "exit":
        # Break game loop
        print("Game Over")
        break

    # Break if all states filled
    if len(correct_states) == len(state_names):
        screen.textinput(title="All states guessed", prompt="All states guessed. Press enter to exit.")
        break

    # Check to see if the answer has been given already
    if answer_state in state_names and answer_state not in correct_states:
        state_index = state_names.index(answer_state)
        state_row = states.iloc[state_index]
        x = state_row.x
        y = state_row.y
        pointer.goto(int(x), int(y))
        pointer.write(answer_state, align="center", font=("Courier", 10, "normal"))
        correct_states.append(answer_state)
        answer_state = screen.textinput(title=f"{len(correct_states)}/{len(state_names)} correct",prompt="Guess a new states name? Enter 'Exit' to exit.").title()
    elif answer_state in correct_states:
        answer_state = screen.textinput(title=f"You already guessed this {answer_state}", prompt="Guess a new states name? Enter 'Exit' to exit.").title()
    else:
        answer_state = screen.textinput(title=f"{answer_state} is not a valid state", prompt="Guess a new states name? Enter 'Exit' to exit.").title()

# Creating a csv file for states that were not guessed
missing_states = [state for state in state_names if state not in correct_states]
pd.DataFrame(missing_states, columns=["state"]).to_csv("states_to_learn.csv", index=False)


