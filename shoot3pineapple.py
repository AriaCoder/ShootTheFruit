import pgzrun
from random import randint
# Shoot(click on) the pineapple. Don't shoot the banana!
pineapple = Actor("pineapple1")
banana = Actor('banana')
score = 0

def draw():
    screen.clear()
    pineapple.draw()
    banana.draw()
    screen.draw.text('Score: ' + str(score), color='white', topleft=(10, 10))

def place_pineapple():
    pineapple.x = randint(10, 800)
    pineapple.y = randint(10, 600)

def place_banana():
    banana.x = randint(10, 800)
    banana.y = randint(10, 600)

def on_mouse_down(pos):
    global score
    if pineapple.collidepoint(pos):
        print("Good shot!")
        score += 1
        place_pineapple()
    elif banana.collidepoint(pos):
        print('You missed. You hit the banana!')
        score -= 1
        place_banana()
    else:
        print("You missed!")
        score -= 1
place_pineapple()    
pgzrun.go()


