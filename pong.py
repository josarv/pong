import turtle

horizontal = 1600
vertical = 900
win = turtle.Screen()
win.title("Pong")
win.bgcolor("black")
win.setup(width=horizontal, height=vertical)
win.tracer(0)

score_a = 0
score_b = 0

paddle_a_pos = -horizontal / 2 + 40
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(paddle_a_pos, 0)

paddle_b_pos = horizontal / 2 - 50
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(paddle_b_pos, 0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("red")  # white
ball.penup()
ball.goto(0, 0)
ball.dx = horizontal * 0.00015
ball.dy = vertical * 0.00015

text_pos = vertical / 2 - 40
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, text_pos)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))

paddle_speed = int(vertical * 0.05)


def paddle_a_up():
    y = paddle_a.ycor()
    y += paddle_speed
    paddle_a.sety(y)
    if paddle_a.ycor() > vertical / 2 + 100:
        paddle_a.sety(-vertical / 2 - 50)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= paddle_speed
    paddle_a.sety(y)
    if paddle_a.ycor() < -vertical / 2 - 50:
        paddle_a.sety(vertical / 2 + 100)


def paddle_b_up():
    y = paddle_b.ycor()
    y += paddle_speed
    paddle_b.sety(y)
    if paddle_b.ycor() > vertical / 2 + 100:
        paddle_b.sety(-vertical / 2 - 50)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= paddle_speed
    paddle_b.sety(y)
    if paddle_b.ycor() < -vertical / 2 - 50:
        paddle_b.sety(vertical / 2 + 100)


win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")

up_bound = vertical / 2 - 10
down_bound = - vertical / 2 + 15
right_bound = horizontal / 2 - 15
left_bound = - horizontal / 2 + 10

paddle_a_bound = - horizontal / 2 - 50

while True:
    win.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    if ball.ycor() > up_bound:
        ball.sety(up_bound)
        ball.dy *= -1
    if ball.ycor() < down_bound:
        ball.sety(down_bound)
        ball.dy *= -1
    if ball.xcor() > right_bound:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
    if ball.xcor() < left_bound:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
    if (paddle_a_pos + 10 < ball.xcor() < paddle_a_pos + 20) and (
            paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(paddle_a_pos + 20)
        ball.dx *= -1
    if (paddle_b_pos - 20 < ball.xcor() < paddle_b_pos - 10) and (
            paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(paddle_b_pos - 20)
        ball.dx *= -1
