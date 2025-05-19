import pgzrun
import random
import time

WIDTH = 600
HEIGHT = 550

sattelites = []

def create_sattelites():
    for i in range(8):
        sat = Actor("sattelite")
        sat.pos = random.randint(30,WIDTH-30),random.randint(30,HEIGHT-30)
        sattelites.append(sat)

def draw():
    number = 1
    screen.blit("space",(0,0))
    for i in sattelites:
        screen.draw.text(str(number),(i.pos[0],i.pos[1]+20))
        number = number + 1
        i.draw()




create_sattelites()
pgzrun.go()
        



