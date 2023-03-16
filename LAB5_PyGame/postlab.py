import pygame as pg
from math import *
pg.init()

win_x, win_y = 1700, 900

screen = pg.display.set_mode((win_x, win_y))

posX = 0
posY = 800
g = 4
u = 1
degree = 60

rad = radians(degree)

time = 0

state = 0

while(1):
    screen.fill((255, 255, 255))

    if pg.mouse.get_pressed()[0] == 1:
        u += 0.1

    posX += u

    if(state==0):
        posY -= u
        if(posY<=400):
            state = 1

    if(state==1):
        posY += u
        if(posY>=800):
            state = 0

    if(posX>win_x):
        posX=0

    pg.draw.circle(screen,(102,178,255),(posX,posY),10)
        
    pg.time.delay(1)

    time += 0.001

    pg.display.update()
    
    for event in pg.event.get():
        if event.type == pg.QUIT: 
            pg.quit()
            exit()
