import turtle
wind = turtle.Screen()
wind.title("ping pong by islam atef")
wind.bgcolor("black")
wind.setup(width=800, height=600)
wind.tracer(0)

# this code for madrap 1
arm1 = turtle.Turtle()
arm1.speed(0)
arm1.shape("square")
arm1.color("white")
arm1.shapesize(stretch_wid=5, stretch_len=1 )
arm1.penup()
arm1.goto(-350, 0)
# this code for madrap 2
arm2 = turtle.Turtle()
arm2.speed(0)
arm2.shape("square")
arm2.shapesize(stretch_len=1, stretch_wid=5)
arm2.color("white")
arm2.penup()
arm2.goto(350, 0)
# this code for ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2.5
ball.dy = 2.5
# for scor
# scor_player_1 = 0
# scor_player_2 = 0
# scor = turtle.Turtle()
# scor.speed(0)
# scor.color("white")
# scor.penup()
# scor.hideturtle()
# scor.goto(0.260)

#functions for playng
#this function for move arm1 up
def arm1_up():
    y=arm1.ycor()
    y+=20
    arm1.sety(y)
#this function for move arm1down
def arm1_down():
    y=arm1.ycor()
    y-=20
    arm1.sety(y)
#this function for move arm2 up
def arm2_up():
    y = arm2.ycor()
    y += 20
    arm2.sety(y)
#this function for move arm2 down
def arm2_down():
    y = arm2.ycor()
    y -= 20
    arm2.sety(y)
# user action
wind.listen()
wind.onkeypress(arm1_up, 'w')
wind.onkeypress(arm1_down, 's')
wind.onkeypress(arm2_up, 'Up')
wind.onkeypress(arm2_down, 'Down')
while True:
    wind.update()
    ball.sety(ball.ycor()+ball.dy)
    ball.setx(ball.xcor() + ball.dx)
    if ball.ycor() > 290:
      ball.sety(290)
      ball.dy *= -1

    if ball.ycor() < -290:
         ball.sety(-290)
         ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
    if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor() < arm2.ycor()+40 and ball.ycor() > arm2.ycor()-40):
        ball.setx(340)
        ball.dx *= -1
    if (ball.xcor()<-340 and ball.xcor()<-350) and (ball.ycor()<arm1.ycor()+40 and ball.ycor() > arm1.ycor() - 40):
        ball.setx(-340)
        ball.dx *=-1

#    # scor.clear()
#   #  scor.write("player 1: "+str(scor_player_1)+ "player 2: "+str(scor_player_2), align="center", font = ("courier", 24, "normal"))
# # else:
# #     scor.clear()
# #     if scor_player_2 == 5:
# #         scor.write("player 2 win", align="center", font = ("courier", 24, "normal"))
# #     else:
# #         scor.write("player 1 win", align="center", font=("courier", 24, "normal"))










'''






import turtle

wind = turtle.Screen()
wind.title("ping pong by islam atef")
wind.bgcolor("black")
wind.setup(width=800, heigh=600)
wind.tracer(0)
# this code for madrap 1
arm1=turtle.Turtle()
arm1.speed(0)
arm1.shape("square")
arm1.shapesize(stretch_len=5, stretch_wid=1)
arm1.color("green")
arm1.penup()
arm1.goto(-350, 0)
# this code for madrap 2
arm2=turtle.Turtle()
arm2.speed(0)
arm2.shape("square")
arm2.shapesize(stretch_len=5, stretch_wid=1)
arm2.color("green")
arm2.penup()
arm2.goto(350, 0)
# this code for ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2.5
ball.dy = 2.5
# for scor
scor_player_1 = 0
scor_player_2 = 0
scor=turtle.Turtle()
scor.speed(0)
scor.color("white")
scor.penup()
scor.hideturtle()
scor.goto(0.260)

#functions for playng
#this function for move arm1 up
def arm1_up():
    y=arm1.ycor()
    y+=20
    arm1.sety(y)
#this function for move arm1down
def arm1_down():
    y=arm1.ycor()
    y-=20
    arm1.sety(y)
#this function for move arm2 up
def arm2_up():
    y = arm1.ycor()
    y += 20
    arm1.sety(y)
#this function for move arm2 down
def arm2_down():
    y = arm1.ycor()
    y -= 20
    arm1.sety(y)










# user action
wind.listen()
wind.onkeypress(arm1_up, 'w')
wind.onkeypress(arm1_down, 's')
wind.onkeypress(arm1_up, 'Up')
wind.onkeypress(arm1_down, 'Down')

while scor_player_1 < 5 and scor_player_2 < 5:
    wind.update()
    ball.sety(ball.ycor()+ball.dy)
    ball.setx(ball.xcor() + ball.dx)
    # border check if exit
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        scor_player_1 += 1
    if ball.xcor() > -390:
        ball.goto(0, 0)
        ball.dx *= -1
        scor_player_2 += 1
    if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor() < arm2.ycor()+40 and ball.ycor() < arm2.ycor()-40):
        ball.setx(340)
        ball.dx *= -1
        if (ball.xcor() > -340 and ball.xcor() <-  350) and (
                ball.ycor() < arm1.ycor() + 40 and ball.ycor() < arm1.ycor() - 40):
            ball.setx(340)
            ball.dx *= -1
    scor.clear()
    scor.write("player 1: "+str(scor_player_1)+ "player 2: "+str(scor_player_2), align="center", font = ("courier", 24, "normal"))
else:
    scor.clear()
    if scor_player_2 == 5:
        scor.write("player 2 win", align="center", font = ("courier", 24, "normal"))
    else:
        scor.write("player 1 win", align="center", font=("courier", 24, "normal"))







'''