import turtle

#Screen settings
screen=turtle.Screen()
screen.title("Pong game")
screen.setup(width=800, height=500)
screen.bgcolor('black')

#Bar A
bar_a = turtle.Turtle()
bar_a.speed(0)
bar_a.shape("square")
bar_a.color("white")
bar_a.shapesize(stretch_wid=6, stretch_len=1)
bar_a.penup()
bar_a.goto(-350, 0)

#Bar B
bar_b = turtle.Turtle()
bar_b.speed(0)
bar_b.shape("square")
bar_b.color("white")
bar_b.shapesize(stretch_wid=6, stretch_len=1)
bar_b.penup()
bar_b.goto(350, 0)


#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.shapesize(stretch_wid=1, stretch_len=1)
ball.penup()
ball.goto(0, 0)
ball.speedX=2
ball.speedY=2

#Scoreboard
score_a=0
score_b=0
scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.penup()
scoreboard.color("White")
scoreboard.hideturtle()
scoreboard.goto(0, 200)
scoreboard.write("Player A: "+str(score_a) +"  Player B: "+ str(score_b), align="center", font=("Arial", 24, "normal"))


#Controlls
def bar_a_up():
    y = bar_a.ycor()
    if(y<=180):
        y+=20
        bar_a.sety(y)

def bar_a_down():
    y = bar_a.ycor()
    if(y>=-180):
        y-=20
        bar_a.sety(y)

def bar_b_up():
    y = bar_b.ycor()
    if(y<=180):
        y+=20
        bar_b.sety(y)

def bar_b_down():
    y = bar_b.ycor()
    if(y>=-180):
        y-=20
        bar_b.sety(y)

#Keyboard binding
screen.listen()
screen.onkeypress(bar_a_up, "w")
screen.onkeypress(bar_a_down, "s")
screen.onkeypress(bar_b_up, "Up")
screen.onkeypress(bar_b_down, "Down")


#Scoreboard

while True:
    screen.update()

    #Ball movement
    ball.setx(ball.xcor() + ball.speedX)
    ball.sety(ball.ycor() + ball.speedY)


    #Border check
    if ball.ycor() == 240:
        ball.speedY *= -1
    if ball.ycor() == -240:
        ball.speedY *= -1
    if ball.xcor() == 390:
        score_b+=1
        ball.goto(0, 0)
        ball.speedX *= -1
        scoreboard.clear()
        scoreboard.write("Player A: " + str(score_a) + "  Player B: " + str(score_b), align="center", font=("Arial", 24, "normal"))
    if ball.xcor() == -390:
        score_a += 1
        ball.goto(0, 0)
        ball.speedX *= -1
        scoreboard.clear()
        scoreboard.write("Player A: " + str(score_a) + "  Player B: " + str(score_b), align="center", font=("Arial", 24, "normal"))

    #Ball touch bar check
    if (ball.xcor() > 330 and ball.xcor()< 340) and (ball.ycor() < bar_b.ycor()+60 and ball.ycor() > bar_b.ycor()-60):
        ball.speedX *= -1
    if (ball.xcor() < -330 and ball.xcor() > -340) and (ball.ycor() < bar_a.ycor()+60 and ball.ycor() > bar_a.ycor()-60):
        ball.speedX *= -1
