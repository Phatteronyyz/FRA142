import pygame as pg
import numpy as np

# initialize pygame
pg.init()

# init display
screen_width, screen_height = 1000, 500
screen2 = pg.display.set_mode((screen_width, screen_height))
screen = pg.display.set_mode((screen_width, screen_height))

# user input
init_x = 50
y_offset = 50
init_y = screen_height - y_offset
init_u = 1.3
init_deg = 45

# default variable
radius = 10
tick = 2
gravity = 1
pixScalex = 1  # Default 2 cm/px
pixScaley = 1
pixScale = 1
time = 0
flag = False
pos_x = init_x
pos_y = init_y
drawpos_y = init_y
rad = np.deg2rad(init_deg)
cir_ux = np.cos(rad)*init_u
cir_uy = np.sin(rad)*init_u
init_time = pg.time.get_ticks()
trajectoryPath = list()


screen.fill((255, 255, 255))
pg.draw.circle(screen, (255, 0, 0), (init_x, init_y), radius)
while True:

    if pg.time.get_ticks() - init_time >= tick:
        init_time = pg.time.get_ticks()
        screen.fill((255, 255, 255))
        
        # print(time)
        print(time)

        time += tick/1000
        if len(trajectoryPath) != 0:
            for i in range(len(trajectoryPath)):
                pg.draw.circle(screen, (0, 255, 0), ((round(trajectoryPath[i][0]*pixScalex)), (round(trajectoryPath[i][1]*pixScaley))), 1)

        pos_x += cir_ux*time
        pos_y -= (cir_uy*time) - (0.5*gravity*(time**2))

        trajectoryPath.append([pos_x, drawpos_y])
        pg.draw.circle(screen, (255, 0, 0), ((round(pos_x*pixScalex)),(round(drawpos_y*pixScaley))), radius * pixScalex)
        pg.draw.line(screen, (0, 255, 0), (init_x , init_y ),(screen_width, init_y )) # X-Axis Datum
        pg.draw.line(screen, (0, 255, 0), (init_x , init_y ), (init_x , 0)) # Y-Axis Datum
        
        pg.display.update()
        if (pos_x * pixScalex) + (radius * pixScale) >= screen_width - (radius * pixScale):
            pixScalex = pixScalex * 0.99
        if (pos_y) - (radius * pixScale) < 20:
            # drawpos_y = 20
            pixScalex = pixScalex * 0.993
        elif (pos_y) - (radius * pixScale) >= 20:
            drawpos_y = pos_y * pixScaley
            
        if pos_y >= init_y:
            while True:
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        pg.quit()
                        exit()

        # if flag is not True and pos_y != init_y:
        #     flag = True
        #     print("Shoot")

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
