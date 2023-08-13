import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S. States")

image = "blank_states_img.gif"  
screen.addshape(image)
turtle.Turtle().shape(image)

data = pandas.read_csv("50_states.csv")
data_name = data["state"].to_list()  
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Guess the state",
                                    prompt="What's another state's name?").title() 

    if answer_state in data_name:
        guessed_states.append(answer_state)
        t = turtle.Turtle()  
        t.penup()
        t.hideturtle()
        # turtle.speed("fastest")
        state_coord = data[data.state == answer_state]
        t.goto(x=int(state_coord["x"]), y=int(state_coord["y"]))
        t.write(answer_state)  
    if answer_state == "Exit":
        missing_states = [state for state in data_name if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

