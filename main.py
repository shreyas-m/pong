from turtle import Screen
import paddle, ball, scoreboard, time

screen = Screen()
left = screen.textinput("Left Player", "Enter left player name.")
right = screen.textinput("Right Player", "Enter right player name.")
screen.bgcolor("black")
screen.screensize(800, 600)
screen.title("Pong")
screen.tracer(0)
screen.listen()

scores = scoreboard.Scoreboard()

l_paddle = paddle.Paddle((-350, 0))
r_paddle = paddle.Paddle((350, 0))
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

ball = ball.Ball()

is_game_on = True

while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    if ball.ycor() > 275 or ball.ycor() < -275:
        ball.bounce_y()
    ball.move()

    # Collision with r_paddle
    if ball.xcor() > 345 or ball.xcor() < -345:
        if (ball.distance(r_paddle) < 50) or (ball.distance(l_paddle) < 50):
            ball.bounce_x()
        else:
            if ball.xcor() > 340:
                scores.l_scored()
            else:
                scores.r_scored()
            ball.reset_position()

    if scores.l_score == 1:
        scoreboard.game_over(left)
        is_game_on = False
    elif scores.r_score == 1:
        scoreboard.game_over(right)
        is_game_on = False

screen.exitonclick()
