#QiQi 4/10 Beginner Pong

import turtle

#Window setup
wn = turtle.Screen()
wn.title("Pong by qiqi")
wn.bgcolor("black")
wn.setup(width= 800, height=600)
wn.tracer(0) #stops window from updating 

#Score
score_a = 0
score_b = 0

#Paddle A
paddle_a = turtle.Turtle() #turtle is the library, Turtle is the class 
paddle_a.speed(0) #animation speed NOT the paddle movement
paddle_a.shape("square")
paddle_a.color("yellow")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0) #location where paddle starts

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("yellow")
paddle_b.shapesize(stretch_wid= 5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.1
ball.dy = 0.1

#Pen 
pen = turtle.Turtle()
pen.speed(0) 
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  Player B: 0", align = "center", font= ("Courier", 18, "normal"))

#Function
def paddle_a_up(): #defining a function
    y = paddle_a.ycor() #return the y cord
    y += 40
    paddle_a.sety(y) #setting y to the new value of y

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 40
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 40
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 40
    paddle_b.sety(y)

#Keyboard Binding
wn.listen() #tells computer to listen for keyboard input 
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

#Main Game Loop (required for every game)
while True:
    wn.update() #allows screen to update everytime loop is ran

    #Ball Movement 
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Boarder 
    if ball.ycor() > 290:
        ball.sety(290) #Sets y cord back to 290
        ball.dy *= -1 #Changes direction, allowing ball to have a bounce affect.
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align = "center", font= ("Courier", 18, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align = "center", font= ("Courier", 18, "normal"))
        
    #Paddle and Ball Collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
    
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1

    
