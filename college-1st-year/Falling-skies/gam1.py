import turtle
import random

wn=turtle.Screen()
wn.title("Falling skies by Akash")
wn.bgcolor("orange")
wn.setup(width=800, height=600)
wn.tracer(0)


#Add the player
player=turtle.Turtle()
player.speed(0)
player.shape("square")
player.color("white")
player.penup()
player.goto(0,-250)
player.direction="stop"
#create list of good guys
good_guys=[]
#add the good guys
for _ in range(20):
    good_guy=turtle.Turtle()
    good_guy.speed(0)
    good_guy.shape("circle")
    good_guy.color("blue")
    good_guy.penup()
    good_guy.goto(0,250)
    good_guy.speed=(random.randint(1,3))
    good_guys.append(good_guy)


# functions
def go_left():
    player.direction="left"
def go_right():
    player.direction="right"

#keyboard binding
wn.listen()
wn.onkeypress(go_left,"Left")
wn.onkeypress(go_right,"Right")

#main game loop
while True:
    #update screen
    wn.update()
    #move the player
    if  player.direction=="left":
        x=player.xcor()
        x-=2
        player.setx(x) 
    if  player.direction=="right":
        x=player.xcor()
        x+=2
        player.setx(x) 
    #move the good guys
    for good_guy in good_guys:
        y=good_guy.ycor()
        y-=(good_guy.speed) 
        good_guy.sety(y)
        #check if off screen
        if y<-300:
            x=random.randint(-380,380)
            y=random.randint(300,400)
            good_guy.goto(x,y)
        if good_guy.distance(player)<20:
            x=random.randint(-380,380)
            y=random.randint(300,400)
            good_guy.goto(x,y)
        

wn.mainloop()