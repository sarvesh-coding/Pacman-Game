import turtle
import random

pacman = turtle.Turtle()
food = turtle.Turtle()
ghost1 = turtle.Turtle()
ghost2 = turtle.Turtle()
game_over = turtle.Turtle()
points = turtle.Turtle()
screen = turtle.Screen()
turtle.bgcolor("black")

turtle.register_shape("Game_over.gif")
game_over.hideturtle()
game_over.shape("Game_over.gif")
turtle.register_shape("Ghost_Enemy.gif")
ghost1.hideturtle()
ghost2.hideturtle()
ghost2.shape("Ghost_Enemy.gif")
ghost1.shape("Ghost_Enemy.gif")

turtle.register_shape("Down_Pacman.gif")

turtle.register_shape("Right_Pacman.gif")
pacman.speed(0)
turtle.register_shape("Left_Pacman.gif")

turtle.register_shape("Up_Pacman.gif")
pacman.shape("Right_Pacman.gif")
ghost1.setpos(350, 100)
ghost2.setpos(350, -100)
ghost2.showturtle()
ghost1.showturtle()
food.fillcolor("red")
food.shape("square")
x = random.randint(-200, 200)
y = random.randint(-200, 200)
food.penup()
food.setpos(x, y)
pacman.penup()
points.hideturtle()
points.setpos(0,250)
score = 0
points.color("white")
points.write(f"Score: {score}", font=("Calibre", 20, "bold"))


def score_calc():
    global score
    score = score+1
    points.color("white")
    points.clear()
    points.write(f"Score: {score}",font=("Calibre",20,"bold"))

def up():
    pacman.shape("Up_Pacman.gif")
    pacman.setheading(90)
    pacman.forward(10)

    if (food.xcor() - 15 <= pacman.xcor() <= food.xcor() + 15 and food.ycor() - 15 <= pacman.ycor() <= food.ycor() + 15):
        food.hideturtle()
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        food.setpos(x, y)
        food.showturtle()
        score_calc()

def down():
    pacman.shape("Down_Pacman.gif")

    pacman.setheading(270)
    pacman.forward(10)
    if (food.xcor() - 15 <= pacman.xcor() <= food.xcor() + 15 and food.ycor() - 15 <= pacman.ycor() <= food.ycor() + 15):
        food.hideturtle()
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        food.setpos(x, y)
        food.showturtle()
        score_calc()


def left():
    pacman.shape("Left_Pacman.gif")
    pacman.setheading(180)
    pacman.forward(10)
    if (food.xcor() - 15 <= pacman.xcor() <= food.xcor() + 15 and food.ycor() - 15 <= pacman.ycor() <= food.ycor() + 15):
        food.hideturtle()
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        food.setpos(x, y)
        food.showturtle()
        score_calc()


def right():
    pacman.shape("Right_Pacman.gif")
    pacman.setheading(0)
    pacman.forward(10)
    if (food.xcor()-15<=pacman.xcor()<=food.xcor()+15 and food.ycor()-15<=pacman.ycor()<=food.ycor()+15):
        food.hideturtle()
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        food.setpos(x, y)
        food.showturtle()
        score_calc()


screen.listen()
screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")

def enemy(back_move):
    stop = 1
    while stop == 1:
        ghost1.penup()
        ghost2.penup()
        if ghost1.xcor() == 350:
            back_move = 0
        if ghost1.xcor() == -350:
            back_move = 1

        if back_move == 0:
            ghost1.backward(10)
            ghost2.backward(10)
        else:
            ghost1.forward(10)
            ghost2.forward(10)
        if (ghost1.xcor()-15<=pacman.xcor()<=ghost1.xcor()+15 and ghost1.ycor()-15<=pacman.ycor()<=ghost1.ycor()+15) or \
                  (ghost2.xcor()-15<=pacman.xcor()<=ghost2.xcor()+15 and ghost2.ycor()-15<=pacman.ycor()<=ghost2.ycor()+15):
            pacman.hideturtle()
            food.hideturtle()
            ghost2.hideturtle()
            ghost1.hideturtle()

            game_over.showturtle()
            stop = 0

back = 0
enemy(back)

turtle.done()