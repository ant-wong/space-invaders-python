# SPACE INVADERS
# Python 3.6
import turtle
import math
import random
import os

# SET UP SCREEN
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
wn.bgpic("spaceman.gif")

# REGISTER SHAPES
turtle.register_shape("spaceship_kirby.gif")
turtle.register_shape("kirby.gif")
turtle.register_shape("heart.gif")

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

# SET SCORE TO 0
score = 0

# DRAW SCORE
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scoreString = "Score: %s" %score
score_pen.write(scoreString, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

# CREATE PLAYER
player = turtle.Turtle()
player.color("pink")
player.shape("kirby.gif")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerSpeed = 15

# NUMBER OF ENEMIES
number_of_enemies = 8
enemies = []

# ADD ENEMIES TO LIST
for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())

for enemy in enemies:
    # CREATE ENEMY
    enemy.color("green")
    enemy.shape("spaceship_kirby.gif")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)

enemySpeed = 12


# PLAYER WEAPON
bullet = turtle.Turtle()
bullet.color("white")
bullet.shape("heart.gif")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletSpeed = 20

# BULLET STATE
# ready
bulletState = "ready"
# fire

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

# FIRE BULLET


def fire_bullet():
    global bulletState
    if bulletState == "ready":
        bulletState = "fire"
        x = player.xcor()
        y = player.ycor()
        bullet.setposition(x, y)
        bullet.showturtle()


def is_collided(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(), 2) + math.pow(t1.ycor()-t2.ycor(), 2))
    if distance < 15:
        return True
    else:
        return False

# KEYBOARD BINDINGS


turtle.listen()
turtle.onkeypress(move_left, "Left")
turtle.onkeypress(move_right, "Right")
turtle.onkeypress(fire_bullet, "space")

# MAIN GAME LOOP
while True:

    for enemy in enemies:
        x = enemy.xcor()
        x += enemySpeed
        enemy.setx(x)

        # ENEMY MOVEMENT
        if enemy.xcor() > 280:
            # MOVE ALL ENEMIES
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemySpeed *= -1

        if enemy.xcor() < -280:
            # MOVE ALL ENEMIES
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemySpeed *= -1

        # CHECK COLLISION
        if is_collided(bullet, enemy):
            # RESET BULLET
            bullet.hideturtle()
            bulletState = "ready"
            bullet.setposition(0, -400)
            # RESET ENEMY
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)
            score += 10
            scoreString = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scoreString, False, align="left", font=("Arial", 14, "normal"))

        # GAME OVER
        if is_collided(player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            print("game over.")
            break

    # MOVE BULLET
    if bulletState == "fire":
        y = bullet.ycor()
        y += bulletSpeed
        bullet.sety(y)

    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletState = "ready"
