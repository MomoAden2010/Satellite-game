import pgzrun
import random
import time

WIDTH = 600
HEIGHT = 550

sattelites = []
next_sattellite = 0
lines = []
num_sattellites = 8
start_time = 0
end_time = 0
total_time = 0

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
    for i in lines:
        screen.draw.line(i[0], i[1], (255,0,0))
        
        




def on_mouse_down(pos):
    global next_sattellite , lines 
    if next_sattellite < num_sattellites:
        if sattelites[next_sattellite].collidepoint(pos):
            if next_sattellite:
                lines.append((sattelites[next_sattellite - 1].pos,sattelites[next_sattellite].pos))
            next_sattellite = next_sattellite + 1
        else:
            lines = []
            next_sattellite = 0
    

    







create_sattelites()
pgzrun.go()
        



