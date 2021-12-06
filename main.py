from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong Game")

# We can use the tracer to make the screen update when we want to with screen.update() method. So that we don't wanna see few things animation and them moving.
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.update()

screen.listen()
screen.onkey(key="Up", fun=r_paddle.go_up)
screen.onkey(key="Down",fun=r_paddle.go_down)
screen.onkey(key="w", fun=l_paddle.go_up)
screen.onkey(key="s", fun=l_paddle.go_down)

game_is_on = True     

times_running = 1

def game():
    global times_running
    time.sleep(ball.move_speed)
    screen.update()
    if times_running % 2 != 0:
        ball.move()
    else:
        ball.opposite_move()
        
    # Detect collision with wall.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle.
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    

    # Detect collision with wall.
    if ball.xcor() > 385: 
        ball.goto(0, 0)
        r_paddle.goto(350, 0)
        l_paddle.goto(-350, 0)
        times_running += 1
        scoreboard.increase_score("r")
        screen.update()
        game()
        ball.move_speed = 0.1
    if ball.xcor() < -385:
        ball.goto(0, 0)
        scoreboard.increase_score("l")
        l_paddle.goto(-350, 0)
        r_paddle.goto(350, 0)
        times_running += 1
        screen.update()
        ball.move_speed = 0.1
        game()
    
screen.update()

while game_is_on:
    screen.update()
    game()
    screen.update()
    

            
    

# Making the screen to stay until we click on it.
screen.exitonclick()
