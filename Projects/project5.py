import turtle, math, time, random
from utils import *

# Section 1: Setup
# TODO - create your player character and any other sprites
# TODO - set your background
# TODO - set the starting value for your variables
sprite_list = []
s1 = create_sprite("puppy", 0, -200)
s2 = create_sprite("rock", 200, 300)
s3 = create_sprite("rock", -250, 300)
s4 = create_sprite("rock", 50, 300)
s5 = create_sprite("rock", -100, 300)
set_background("park")

points = 15


def move_left_1():
    x = s1.xcor() -30
    y = s1.ycor()
    s1.goto(x, y)
window.onkeypress(move_left_1, "c")

def move_right_1():
    x = s1.xcor()+ 30
    y = s1.ycor()
    s1.goto(x, y)
window.onkeypress(move_right_1, "e")

def move_down2():
    x = s2.xcor()
    y = s2.ycor()-1
    s2.goto(x, y)
    if s2.ycor() < -300:
     s2.goto(x,300)
def move_down3():
    x = s3.xcor()
    y = s3.ycor()-1
    s3.goto(x, y)
    if s3.ycor() < -300:
     s3.goto(x,300)
def move_down4():
    x = s4.xcor()
    y = s4.ycor()-1
    s4.goto(x, y)
    if s4.ycor() < -300:
     s4.goto(x,300)
def move_down5():
    x = s5.xcor()
    y = s5.ycor()-1
    s5.goto(x, y)
    if s5.ycor() < -300:
     s5.goto(x,300)

# Section 2: Controls
# TODO - define your controls
# TODO - pick keys for each control

# Section 3: Game Loop
window.listen()
for i in range(10000000000):
    
    # TODO - add code for automatic actions
    if i > 100 :
        move_down2()
    if i > 200 :
        move_down3()
    if i > 400 :
        move_down4()
    if i > 600 :
        move_down5()

    if get_distance(s2, s1)< 100:
       points -= 1

    # TODO - make an if statement for ending the game
    if points < 0:
       break
    
    time.sleep(0.01)
    window.update()
    

	
print("Game Over")