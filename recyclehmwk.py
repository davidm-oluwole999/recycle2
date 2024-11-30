import pgzrun
import random

WIDTH= 800
HEIGHT= 600

ITEMS= ["byron","mortis","EMZ","frank"]

GAME_STAGE= "start"
CURRENT_LEVEL= 1
FINAL_LEVEL= 6
START_SPEED= 10
items= []
animations= []

def display_message(msg):
    screen.draw.text(msg, fontsize= 45, center= (WIDTH/2, HEIGHT/2), color= "red")


def draw():
    global ITEMS, GAME_STAGE, CURRENT_LEVEL, FINAL_LEVEL, START_SPEED
    screen.clear()
    screen.blit("desert",(0,0))
    if GAME_STAGE == "over":
        display_message("Game Over!/n Try Again!")
    elif CURRENT_LEVEL == FINAL_LEVEL or GAME_STAGE == "win" :
        display_message("You Won!/n Well Done!")
        
pgzrun.go()