from time import sleep
from snake_game_utils import *
score = 0
high_score = 0
speed = 0.3


def change_dir_to_up():
    if snake_head.direction != "down":
        snake_head.direction = "up"


def change_dir_to_left():
    if snake_head.direction != "right":
        snake_head.direction = "left"


def change_dir_to_right():
    if snake_head.direction != "left":
        snake_head.direction = "right"


def change_dir_to_down():
    if snake_head.direction != "up":
        snake_head.direction = "down"


def reset():
    global score
    file = open("snake_scores.txt", "w")
    file.write(str(high_score))
    file.close()
    score = 0
    snake_head.goto(0, 0)
    snake_head.direction = ""
    for body in snake_body:
        body.hideturtle()
    snake_body.clear()


window = make_screen()

snake_head = make_turtle("square", "black")
snake_head.direction = ""

food = make_turtle("circle", "red")
change_food_position(food)

score_board = make_turtle()
score_board.hideturtle()
score_board.goto(0, 260)

window.listen()
window.onkeypress(change_dir_to_up, "Up")
window.onkeypress(change_dir_to_left, "Left")
window.onkeypress(change_dir_to_right, "Right")
window.onkeypress(change_dir_to_down, "Down")


snake_body = []
while True:
    window.update()
    score_board.clear()
    score_board.write(f"SCORE:{score}, high score:{high_score}", align="center",
                      font=("Arial", 22))

    if snake_head.distance(food) < 20:
        score += 1
        if score > high_score:
            high_score = score

        change_food_position(food)
        new_body = make_turtle("square", "grey")
        snake_body.append(new_body)

    for i in range(len(snake_body) - 1, 0, -1):
        prev_x = snake_body[i-1].xcor()
        prev_y = snake_body[i-1].ycor()
        snake_body[i].goto(prev_x, prev_y)

    if len(snake_body) > 0:
        head_x = snake_head.xcor()
        head_y = snake_head.ycor()
        snake_body[0].goto(head_x, head_y)

    if snake_head.xcor() > 290 or snake_head.xcor() < -290 or snake_head.ycor() > 290 or snake_head.ycor() < -290:
        reset()

    move_snake(snake_head)
    try:
        speed = 0.2/score*2.5
        print(speed)
        sleep(speed)
        # sleep(0.2*(1+score/10))
    except:
        sleep(speed)
