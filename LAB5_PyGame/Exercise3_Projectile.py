import pygame as pg
from math import *
pg.init()

win_x, win_y = 1700, 900

screen = pg.display.set_mode((win_x, win_y))

# posX = int(input())
# posY = int(input())
# u = int(input())
# degree = int(input())

posX = 30
posY = 800
g = 1
u = 1
degree = 60

rad = radians(degree)

time = 0

st = 0

while(1):
    screen.fill((255, 255, 255))

    posX += u * cos(rad) * time
    posY -= (u * sin(rad) * time) - (0.5 * g * time**2)

    pg.draw.circle(screen,(102,178,255),(posX,posY),10)

    print(time)
        
    pg.time.delay(0)
    
    time += 0.001

    pg.display.update()
    
    for event in pg.event.get():
        if event.type == pg.QUIT: 
            pg.quit()
            exit()
