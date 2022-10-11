from turtle import Screen
import turtle as t

timmy_the_turtle = t.Turtle

for _ in range(15):
    timmy_the_turtle.forward(10)
    timmy_the_turtle.penup()
    timmy_the_turtle.forward(10)
    timmy_the_turtle.pendown()

screen = Screen()
screen.exitonclick()