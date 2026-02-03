import turtle

#Setup the window
window = turtle.Screen()
window.title("Ping Pong")
window.setup(width=800, height=600)
window.tracer(0)
window.bgcolor(.1, .1, .1)

#Setup game objects
#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.shapesize(stretch_wid=1, stretch_len=1)
ball.goto(0, 0)
ball.penup()
ball.dx, ball.dy = 1,1
ball_speed = 0.1

#Centre line
center_line = turtle.Turtle()
center_line.speed(0)
center_line.shape("square")
center_line.color("white")
center_line.shapesize(stretch_wid=25, stretch_len=0.1)
center_line.penup()
center_line.goto(0, 0)

#Player 1 : Baha
player1 = turtle.Turtle()
player1.speed(0)
player1.shape("square")
player1.shapesize(stretch_wid=5, stretch_len=1)
player1.color("blue")
player1.penup()
player1.goto(-350, 0)

#Player 2 : Emma
player2 = turtle.Turtle()
player2.speed(0)
player2.shape("square")
player2.shapesize(stretch_wid=5, stretch_len=1)
player2.color("red")
player2.penup()
player2.goto(350, 0)

#Score text
score_text = turtle.Turtle()
score_text.speed(0)
score_text.color("white")
score_text.penup()
score_text.goto(0, 260)
score_text.write("Baha1: 0   Baha2: 0", align="center", font=("Courier", 24, "normal"))
score_text.hideturtle()
p1_score = 0
p2_score = 0 

#Players Movement
player_speed = 20
def p1_up():
    player1.sety(player1.ycor() + player_speed)

def p1_down():
    player1.sety(player1.ycor() - player_speed)

def p2_up():
    player2.sety(player2.ycor() + player_speed)

def p2_down():
    player2.sety(player2.ycor() - player_speed)

#Get users input
window.listen()
window.onkeypress(p1_up, "z")
window.onkeypress(p1_down, "s")
window.onkeypress(p2_up, "Up")
window.onkeypress(p2_down, "Down")



#Game loop ========================================
while True:
    window.update()


    #Move the ball
    ball.setx(ball.xcor() + ball.dx * ball_speed)
    ball.sety(ball.ycor() + ball.dy * ball_speed)

    #Ball Borders
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    #Ball & Players collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < player2.ycor() + 50 and ball.ycor() > player2.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < player1.ycor() + 50 and ball.ycor() > player1.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1

    #Score update
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        p1_score += 1
        score_text.clear()
        score_text.write(f"Baha: {p1_score}   Emma: {p2_score}", align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        p2_score += 1
        score_text.clear()
        score_text.write(f"Baha: {p1_score}   Emma: {p2_score}", align="center", font=("Courier", 24, "normal"))