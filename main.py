# SPACE INVADERS
# Python 3.6
import turtle
import os

# SET UP SCREEN
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")

# DRAW BORDER
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

# CREATE PLAYER
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerSpeed = 15

# CREATE ENEMY
enemy = turtle.Turtle()
enemy.color("red")
enemy.shape("circle")
enemy.penup()
enemy.speed(0)
enemy.setposition(-200, 250)

enemySpeed = 3

# MOVE PLAYER


def move_left():
    x = player.xcor()
    x -= playerSpeed
    if x < -280:
        x = -280
    player.setx(x)


def move_right():
    x = player.xcor()
    x += playerSpeed
    if x > 280:
        x = 280
    player.setx(x)

# KEYBOARD BINDINGS


turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")

# MAIN GAME LOOP
while True:

    x = enemy.xcor()
    x += enemySpeed
    enemy.setx(x)

    if enemy.xcor() > 280:
        y = enemy.ycor()
        y -= 40
        enemySpeed *= -1
        enemy.sety(y)

    if enemy.xcor() < -280:
        y = enemy.ycor()
        y -= 40
        enemySpeed *= -1
        enemy.sety(y)

delay = input("Press enter to finish.")

