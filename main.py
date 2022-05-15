import random
from turtle import Screen, textinput, Turtle

race_is_on = False
turtle_bet = textinput(title="Make your bet", prompt="Which turtle do you think will win the race? Enter a color: ")
screen = Screen()
screen.setup(width=500, height=400)

rainbow_color = ["red", "yellow", "green", "blue", "purple", "orange"]
position = [-100, -70, -40, -10, 20, 50]
all_turtles = []

if turtle_bet:
    race_is_on = True

for index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(rainbow_color[index])
    new_turtle.penup()
    new_turtle.setposition(x=-230, y=position[index])
    all_turtles.append(new_turtle)

while race_is_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_is_on = False
            winning_color = turtle.fillcolor()
            if winning_color == turtle_bet.lower():
                print(f"You've won! The {winning_color} turtle got the first place!")
            else:
                print(f"You lose! The {winning_color} turtle got the first place! Your bet was {turtle_bet}")
        turtle.forward(random.randint(0,10))

screen.exitonclick()
