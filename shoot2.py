import math
import pgzrun
from random import randint

WIDTH = 1440
HEIGHT = 855

CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2
CENTER = (CENTER_X, CENTER_Y)

music.play("background.mp3")
fruits = []
for fruit in fruits:
    fruit.x = randint(10, WIDTH)
    fruit.y = randint(10, HEIGHT)
game_over = False
score = 0
winning = False
message = ""
lives = 3
duration2 = 0
retried = False
restarted = False
retrybutton = Actor("retrybutton")
restartbutton = Actor("restartbutton")
boomed = False
text_boom = ''
speed = 300
fill = False
fill_purple = False

def restart_false():
    global restarted
    restarted = False

def retry():
    global retried, message, retrybutton, fill
    screen.clear()
    fruits = []
    fruits = [Actor("apple"), Actor("orange"), Actor("banana"), Actor("peach"),
              Actor("lemon"), Actor("grapes"), Actor("pear"), Actor("plum"), Actor("watermelon")]
    fill = True
    retried = True
    message = ""
    retrybutton = Actor("retrybutton", pos=CENTER)

def restarting():
    global restarted, message, restartbutton
    restarted = True
    message = ""
    restartbutton = Actor("retrybutton copy", pos=CENTER)

def restart():
    global score, winning, message, lives, game_over, fruits, duration2, retrybutton, retried, restarted, restartbutton, bomb, boomed
    fill_purple = True
    music.play("background.mp3")
    score = 0
    winning = False
    message = ""
    fill = False
    lives = 3
    retried = False
    game_over = False
    fruits = []
    fruits = [Actor("apple"), Actor("orange"), Actor("banana"), Actor("peach"),
              Actor("lemon"), Actor("grapes"), Actor("pear"), Actor("plum"), Actor("watermelon")]
    bomb = Actor("bomb")
    for fruit in fruits:
        fruit.x = randint(10, WIDTH)
        fruit.y = randint(10, HEIGHT)
    bomb.x = randint(10, WIDTH)
    bomb.y = randint(10, HEIGHT)
    if retried:
        retrybutton = None
    if restarted:
        retrybutton = None
        restarted = False
    boomed = False
    speed = 40
    glide()

def draw():
    global game_over, fruits, score, lives, message, winning, retried, retrybutton, restarted, restartbutton, bomb, text_boom, fill, fill_purple, boomed
    screen.clear()
    screen.fill("dark violet")
    if fill_purple:
        screen.fill_('dark violet')
        fill_purple = False
    if not game_over:
        if not boomed:
            if not winning:
                for fruit in fruits:
                    fruit.draw()
                bomb.draw()
    screen.draw.text(message, fontsize=60, center=CENTER, color="black")
    if winning or not game_over:
        screen.draw.text("Score: " + str(score), color="black", topleft=(10, 10))
        screen.blit("life-count", (0, HEIGHT - 30))
        screen.draw.text(str(lives), fontsize=40, pos=(30, HEIGHT - 30), color="black")
    if boomed:
        message = 'GAME OVER! You blew up!'
        lives = 0
        screen.fill('black')
        screen.draw.text(message, fontsize=60, center=CENTER, color='white')
        clock.schedule(retry, 3.0)
    if retried:
        retrybutton.draw()
    if restarted:
        restartbutton.draw()
    elif restarted == False:
        restartbutton = None

def boom():
    global bomb, boomed
    sounds.boomboom.play()
    boomed = True
    bomb = None
    game_over_boom()
       
def on_mouse_down(pos):
        global score, speed, winning, retried, retrybutton
        hit = False
        if not game_over and not winning:
            for fruit in reversed(fruits):
                if fruit.collidepoint(pos):
                     sounds.splat.play()
                     hit = True
                     speed += 20
                     score += 1
                     fruits.remove(fruit)
                     if fruits == []:
                         winning = True
                         handle_end()
                     break
                if not boomed:
                    if bomb.collidepoint(pos):
                        boom()
            if not hit:
                subtract_life()
        if retried:
            if retrybutton.collidepoint(pos):
                retrybutton = None
                restart()
        if restarted:
            if restartbutton.collidepoint(pos):
                restart()

def setup_screen():
    screen.clear()
    screen.fill("dark violet")

def you_missed():
    global lives, message
    lives -= 1
    message = "You missed."
    sounds.boing.play()
    glide()
    clock.schedule(set_message_to_blank, 2.0)

def game_over1():
    global game_over, message
    game_over = True
    message = "GAME OVER!"
    music.stop()
    sounds.gameover.play()
    clock.schedule(retry, 3.0)

def game_over_boom():
    screen.fill('black')
    music.stop()
    sounds.gameover.play()
    clock.schedule(retry, 3.0)
    
def subtract_life():
    if not winning:
        if lives > 0:
            you_missed()
        if lives == 0:
            game_over1()
                
def set_message_to_blank():
        global message
        if not game_over:
            message = ""

def glide():
    for fruit in fruits:
        if not hasattr(fruit, 'animation') or not fruit.animation.running:
            if not game_over:
                glide_one(fruit)
    if not hasattr(bomb, 'animation') or not bomb.animation.running:
        if not game_over:
            glide_one(bomb)

def glide_one(item):
    if not boomed:
        new_x = randint(10, WIDTH)
        new_y = randint(10, HEIGHT)
        news = (new_x, new_y)
        distance = item.distance_to(news)
        item.animation = animate(item, pos=news, duration=distance / speed, on_finished=glide)

def handle_end():
    global message
    setup_screen()
    message = "YOU WON!"
    music.stop()
    sounds.victory.play()
    clock.schedule(restarting, 3.0)



def main():
    restart()    
    glide()
    pgzrun.go()

main()
