import pgzrun
import random
import time 
WIDTH = 700
HEIGHT = 500
TITLE = "connecting satellites"
start = time.time()
total_time = 0
#satellites
total = [] 
number = 8
index = 0
lines = []
for i in range(number):
    satellite = Actor("satellite")
    satellite.pos = (random.randint(50,650),random.randint(50,450)) 
    total.append(satellite)
#drawing
def draw():
    global total_time
    screen.blit("space backround 2",(0,0))
    n = 1
    for satellite in total:
        satellite.draw()
        screen.draw.text(str(n),(satellite.pos[0],satellite.pos[1]+20))
        n = n + 1
    for line in lines:
        screen.draw.line(line[0],line[1],"white")
    if index < 8:
        total_time = time.time() - start 
    screen.draw.text("time :"+str(round(total_time,1)),(50,50))
def update():
    pass
def on_mouse_down(pos): 
    global lines,index 
    if index < 8:
        if total[index].collidepoint(pos):
            if index > 0:
                lines.append((total[index-1].pos,total[index].pos))
            index = index + 1 
        else:
            index = 0
            lines = []









pgzrun.go()
