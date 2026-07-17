from turtle import *

# def draw_shape(x,y):
#     sides = int(sc.numinput("sides", "enter sides number"))
#     color = sc.textinput("color", "enter the color")
#     t.penup()
#     t.goto(x,y)
#     t.pendown()
#     t.color(color)
#     t.begin_fill()
#     for _ in range(sides):
#         t.fd(80)
#         t.left(360/sides)
#     t.end_fill()
sc = Screen()
t = Turtle()
# t.shape("turtle")
# t.goto(100, 100)
# t.write(1, font=("arial", 22))
# t.goto(100, 200)
# sc.onclick(draw_shape)
t.speed("fastest")
def draw_axis():
    for i in range(5):
        t.write(i, align="right")
        t.fd(i + 50)

draw_axis()
t.stamp()

t.home()
t.left(90)
draw_axis()
t.stamp()
t.home()
t.left(180)
draw_axis()
t.stamp()
t.home()
t.right(90)
draw_axis()
done()