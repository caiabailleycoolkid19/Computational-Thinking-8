import turtle, math, time, random
from utils import *

# Section 1: Setup
# TODO - create your player character and any other sprites
# TODO - set your background
# TODO - set the starting value for your variables
sprite_list = []
s1 = create_sprite("puppy", 0, -200)
s2 = create_sprite("rock", 100, 300)
s3 = create_sprite("rock", -250, 300)
s4 = create_sprite("rock", 50, 300)
s5 = create_sprite("rock", -100, 300)
set_background("park")

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



# Section 2: Controls
# TODO - define your controls
# TODO - pick keys for each control

# Section 3: Game Loop
window.listen()
for i in range(10000000000):
    
    # TODO - add code for automatic actions


    # TODO - make an if statement for ending the game

    
    time.sleep(0.01)
    window.update()
    

	
print("Game Over")