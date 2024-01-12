from turtle import Screen, Turtle
from random import randint
def make_screen():
    window = Screen()
    window.title("Snake Game")
    window.bgcolor("blue")
    window.setup(width=600, height=600)
    window.tracer(0)
    return window

def make_turtle(shape="square", color="white"):
    turtle_object = Turtle()
    turtle_object.shape(shape)
    turtle_object.color(color)
    turtle_object.speed("fastest")
    turtle_object.penup()
    return turtle_object

def change_food_position(food):
    food_x = randint(-270, 270)
    food_y = randint(-270, 270)
    food.goto(food_x, food_y)


def move_snake(snake_head):
    if snake_head.direction == "up":
        yposition = snake_head.ycor()
        snake_head.sety(yposition + 20)
    if snake_head.direction == "down":
        yposition = snake_head.ycor()
        snake_head.sety(yposition - 20)
    if snake_head.direction == "left":
        xposition = snake_head.xcor()
        snake_head.setx(xposition - 20)
    if snake_head.direction == "right":
        xposition = snake_head.xcor()
        snake_head.setx(xposition + 20)