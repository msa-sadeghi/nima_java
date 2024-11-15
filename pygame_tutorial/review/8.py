import turtle
turtle.speed("fastest")
turtle.ht()
turtle.pencolor("purple")
turtle.pensize(2)
def draw_parallel_lines():
    turtle.penup()
    turtle.goto(-250, 100)
    turtle.pendown()
    turtle.goto(250, 100)
    turtle.penup()
    
    turtle.goto(-250, -100)
    turtle.pendown()
    turtle.goto(250, -100)
    turtle.penup()
    


def another_line():
    turtle.goto(-100, 150)
    turtle.pendown()
    turtle.goto(100, -150)
    turtle.penup()


def draw_angles():
    turtle.goto(-85, 130)
    turtle.color("red")
    turtle.pensize(3)
    turtle.pendown()
    for i in range(18):
        turtle.right(4)
        turtle.fd(3)
    turtle.color("green")
    for i in range(10):
        turtle.right(4)
        turtle.fd(3)
    turtle.penup()
    turtle.goto(-50, 135)
    turtle.color("red")
    turtle.write(120, font=("arial", 16))
    turtle.setheading(0)
    turtle.goto(55, -80)
    turtle.color("red")
    turtle.pensize(3)
    turtle.pendown()
    for i in range(14):
        turtle.right(4)
        turtle.fd(3)
    turtle.color("green")
    for i in range(14):
        turtle.right(4)
        turtle.fd(3)
    turtle.penup()
    turtle.goto(85, -75)
    turtle.color("red")
    turtle.write(120, font=("arial", 16))





draw_parallel_lines()
another_line()
draw_angles()
turtle.done()