# W = Forwards
# S = Backwards
# A = Counter Clockwise
# D = Clockwise
# C = Clear
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color.").lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

y_positions = -100
all_turtles = []

for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color)
    new_turtle.goto(-230, y_positions)
    new_turtle.speed("fastest")
    y_positions += 50
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You've won! The {winner} turtle is the winner!")
            else:
                print(f"You've lost! The {winner} turtle is the winner!")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
screen.exitonclick()
