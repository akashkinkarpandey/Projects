import turtle
import random
import winsound

score=0
lives=10

wn=turtle.Screen()
wn.title("Falling skies by Akash")
wn.bgcolor("orange")
wn.bgpic("background.gif")
wn.setup(width=800, height=600)
wn.tracer(0)

wn.register_shape("deer_left.gif")
wn.register_shape("deer_right.gif")
wn.register_shape("hunter.gif")
wn.register_shape("nut.gif")
wn.register_shape("selmon.gif")


#Add the player
player=turtle.Turtle()
player.speed(0)
player.shape("selmon.gif")
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
    good_guy.shape("deer_right.gif")
    good_guy.color("red")
    good_guy.penup()
    good_guy.goto(-100,250)
    good_guy.speed=(random.randint(1,3))
    good_guys.append(good_guy)
#create list of bad guys
bad_guys=[]
#add the bad guys
for _ in range(20): 
    bad_guy=turtle.Turtle()
    bad_guy.speed(0)
    bad_guy.shape("deer_left.gif")
    bad_guy.color("blue")
    bad_guy.penup()
    bad_guy.goto(100,250)
    bad_guy.speed=(random.randint(1,3))
    bad_guys.append(bad_guy)

#make the pen
pen=turtle.Turtle()
pen.hideturtle()
pen.shape("square")
pen.color("white")
pen.penup()
pen.goto(0,260)
font=("Courier",24,"normal")
pen.write("Score:{} Lives :{}".format(score,lives),align="center",font=font)
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
    #Move the good guys
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
            winsound.PlaySound("laser.wav", winsound.SND_ASYNC)
            x=random.randint(-380,380)
            y=random.randint(300,400)
            good_guy.goto(x,y)
            score+=10
            pen.clear()
            pen.write("Score:{} Lives :{}".format(score,lives),align="center",font=font)
    #Move the bad guys
    for bad_guy in bad_guys:
        y=bad_guy.ycor()
        y-=(bad_guy.speed) 
        bad_guy.sety(y)
        #check if off screen
        if y<-300:
            x=random.randint(-380,380)
            y=random.randint(300,400)
            bad_guy.goto(x,y)
        if bad_guy.distance(player)<20:
            x=random.randint(-380,380)
            y=random.randint(300,400)
            bad_guy.goto(x,y)
            score-=10
            lives-=1
            pen.clear()
            pen.write("Score:{} Lives :{}".format(score,lives),align="center",font=font)
        

wn.mainloop()