import pgzrun
from random import randint
# Shoot(click on) the orange. Don't shoot the peach!
orange = Actor("orange1")
peach = Actor('peach')
score = 0

def draw():
    screen.clear()
    orange.draw()
    peach.draw()
    screen.draw.text('Score: ' + str(score), color='white', topleft=(10, 10))

def place_orange():
    orange.x = randint(10, 800)
    orange.y = randint(10, 600)

def place_peach():
    peach.x = randint(10, 800)
    peach.y = randint(10, 600)

def on_mouse_down(pos):
    global score
    if orange.collidepoint(pos):
        print("Good shot!")
        score += 1
        place_orange()
    elif peach.collidepoint(pos):
        print('You missed. You hit the peach!')
        score -= 1
        place_peach()
    else:
        print("You missed!")
        score -= 1
place_orange()    
pgzrun.go()


