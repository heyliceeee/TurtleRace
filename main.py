import random
from turtle import Turtle, Screen


screen = Screen()
screen.setup(500, 400) # setup the screen

all_turtles = []
colors = ["red", "blue", "orange", "yellow", "green", "purple"]
user_bet = screen.textinput("make your bet", f"who will win this race? enter a color: {colors}").lower() # create textbox
y_positions = [-70, -40, -10, 20, 50, 80]
is_race_on = False # true if race start, otherwise false

def instance_turtles():
    """
    instance 6 turtles, set colors and set positions
    """
    for current_turtle in range(0, 6):
        new_turtle = Turtle("turtle")  # create turtle
        new_turtle.color(colors[current_turtle])  # set color
        new_turtle.penup()  # no draw while move
        new_turtle.goto(-230, y_positions[current_turtle])  # set position (left side screen)

        all_turtles.append(new_turtle) # add new_turtle in list
def race_start():
    """
    move turtles randomly until goal
    """
    is_race_on = True  # race start
    while is_race_on: # while race happends
        for turtle in all_turtles: # in each turtle
            if turtle.xcor() > 230: # check if current turtle come goal
                is_race_on = False # race stop
                winning_color = turtle.pencolor()
                if winning_color == user_bet: # check if winner is user bet
                    print(f"you have won! the {winning_color} turtle is the winner!")
                else:
                    print(f"you have lost! the {winning_color} turtle is the winner!")

            rand_distance = random.randint(0, 10) # current turtle move randomly between 0 and 10
            turtle.forward(rand_distance) # current turtle move forward random steps

if user_bet in colors: # if user enter valid color
    instance_turtles() # instance 6 turtles
    race_start() # move turtles randomly until goal
screen.exitonclick()