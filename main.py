import turtle
from turtle import Turtle, Screen


screen = Screen()
screen.setup(500, 400) # setup the screen

colors = ["red", "blue", "orange", "yellow", "green", "purple"]
user_bet = screen.textinput("make your bet", f"who will win this race? enter a color: {colors}").lower() # create textbox
y_positions = [-70, -40, -10, 20, 50, 80]


if user_bet in colors: # if user enter valid color
    for current_turtle in range(0, 6):
        tim = Turtle("turtle") # create turtle
        tim.color(colors[current_turtle]) # set color
        tim.penup() # no draw while move
        tim.goto(-230, y_positions[current_turtle]) # set position

# instance 6 turtles of 6 different colors (purple, blue, green, yellow, orange and red)
# the turtles start in left side screen and run different steps until go right side screen
# the first turtle come right side screen is the winner. then print if im a looser or not




screen.exitonclick()