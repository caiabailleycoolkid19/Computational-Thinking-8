import turtle, time, random
from utils import *

# Section 1 - setup
# The goal of the game is to make as many cookies and money appear as possible
set_background("bakery")
cookie = 0
money = 0

# OPTIONAL: use this invisible alien to say a message
# message_sprite = create_sprite("alien", -200,200)
# message_sprite.hideturtle()

# Section 2 - controls
def increase_cookie ():
    global cookie
    cookie += 1
    x = random.randint (-200,200)
    y = random.randint (-200,200)
    create_sprite("cookie",x,y)
window.onkeypress(increase_cookie, "space") 
# When clicking the "space" key you increase the amount of cookies  

def increase_money():
    global money
    money += 1
    x = random.randint (-200,200)
    y = random.randint (-200,200)
    create_sprite("money",x,y)
window.onkeypress(increase_money, "c")
# When clicking the "c" key you increase money amount 

# Section 3 - game loop
window.listen()
for i in range(1000000000):

    time.sleep(0.01)
    window.update()