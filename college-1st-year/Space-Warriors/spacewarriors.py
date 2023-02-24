import turtle
import os
import math
import random
import winsound

wn =turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
wn.bgpic("space invaders.gif")

#register shape
turtle.register_shape("player.gif")
turtle.register_shape("invader.gif")



#Draw border

border_pen=turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pensize(3)
border_pen.pendown()

for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)

border_pen.hideturtle()

#set score to zero
score=0
#Draw the score
score_pen=turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290,268)
scorestring="Score: %s" %score
score_pen.write (scorestring, align = "left", font = ("Arial", 14, "normal"))
score_pen.hideturtle()


#create the player
player =turtle.Turtle()
player.color("blue")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)

playerspeed=15




#choose number of enemies
number_of_enemies=5
#create empty list of enemies
enemies=[]
#add enemies to list
for i in range(number_of_enemies):
   #create enemy
   enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color("red")
    enemy.shape("invader.gif")
    enemy.penup()
    enemy.speed(0)
    x=random.randint(-200,200)
    y=random.randint(100, 250)
    enemy.setposition(x, y)

enemyspeed=2

#create players bullet
bullet=turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()

bulletspeed=20

#define bullet state
#ready-ready to fire
#fire =firing
bulletstate="ready"



#move the player left right
def move_left():
    x=player.xcor()
    x -=playerspeed
    if x <-280:
        x=-280
    player.setx(x)

def move_right():
    x=player.xcor()
    x +=playerspeed
    if x >280:
        x=280
    player.setx(x)

def fire_bullet():
    #declare bulletstate as global if needed
    global bulletstate

    if bulletstate=="ready":
        winsound.PlaySound("laser.wav", winsound.SND_ASYNC)
        bulletstate="fire"
        x=player.xcor()
        y=player.ycor()+10
        bullet.setposition(x,y)
        bullet.showturtle()

def isCollision(t1, t2):
    distance=math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance<15:
        return True
    else:
        return False

#create keyboard bindings
turtle.listen()
turtle.onkey(move_left,"Left")
turtle.onkey(move_right,"Right")
turtle.onkey(fire_bullet,"space")

#Main game loop

while True:
     wn.update()

     for enemy in enemies:
         #Move the enemies
         x=enemy.xcor()
         x+=enemyspeed
         enemy.setx(x)

         if enemy.xcor() >280:
             #move all enemies down
             for e in enemies:
                y=e.ycor()
                y-=40
                e.sety(y)
             #change enemy direction
             enemyspeed*=-1

         if enemy.xcor()<-280:
             #move all enemies down
             for e in enemies:
                 y=e.ycor()
                 y-=40
                 e.sety(y)
             #change enemy direction
             enemyspeed*=-1


         if isCollision(bullet, enemy):
             # Reset the bullet
             winsound.PlaySound("explosion.wav", winsound.SND_ASYNC)
             bullet.hideturtle()
             bulletstate = "ready"
             bullet.setposition(0, -400)
             # reset the enemy
             enemy.setposition(-200, 250)
             x = random.randint(-200, 200)
             y = random.randint(100, 250)
             enemy.setposition(x, y)
             #update score
             score+=10
             scorestring="Score: %s" %score
             score_pen.clear()
             score_pen.write(scorestring, align="left", font=("Arial", 14, "normal"))


         if isCollision(player, enemy):
             winsound.PlaySound("explosion.wav", winsound.SND_ASYNC)
             player.hideturtle()
             enemy.hideturtle()
             print("Game Over")
             break

     #move bbullet
     if bulletstate == "fire":
          y=bullet.ycor()
          y+=bulletspeed
          bullet.sety(y)
     #check to see if bullet has gone to top
     if bullet.ycor() > 275:
         bullet.hideturtle()
         bulletstate="ready"

         # check for colision between bullet and enemy







