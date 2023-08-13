from turtle import Turtle, Screen
import random

def main():
    
    
    screen = Screen()
    screen.setup(width=500, height=400)
    user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a color: ")
    colors = ['red', 'blue', 'green', 'purple', 'orange', 'yellow']
    y_position = [-100, -60, -20, 20, 60, 100]
    all_turtles = []
    
    for turtle in range(6):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(colors[turtle])
        new_turtle.penup()
        new_turtle.goto(x=-235, y=y_position[turtle])
        all_turtles.append(new_turtle)



    is_race = False
    if user_bet:
        is_race = True
    
    while is_race:
        for turtle in all_turtles:
            distance = random.randint(0, 10)
            turtle.forward(distance)
    
            if turtle.xcor() > 230:
                winning_color = turtle.pencolor()
                is_race = False
    
                if winning_color == user_bet:
                    print(f"You won! Congratulations. The winner was {winning_color} turtle.")
    
                else:
                    print(f"You lost! The winner was {winning_color} turtle.")
    
    

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
