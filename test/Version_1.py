import pygame as pg
import math as m
import random as r

pg.init()
# screen -------------------------------------------------------------- #
win_x, win_y = 1530, 800
screen = pg.display.set_mode((win_x, win_y))
# gamerule  -------------------------------------------------------------- #
# True : move around freely, False : miss a note and fail (not done)
gamerule_tester = True
gamerule_show_reference_axis = False
# position -------------------------------------------------------------- # Axis (x,y) = (right,down) | Axis (i,j) = (right,up)
posX_B, posY_B, posX_R, posY_R = 0, 0, 0, 0
refX, refY = win_x/2, win_y/2
Center_B, Center_R = 100, 0
# count -------------------------------------------------------------- #
deg = 0
path_position = 0
Background_color_decay = 0
# condition -------------------------------------------------------------- #
cx = 0
cy = 0
# lists -------------------------------------------------------------- #
# 0: start, 1: right, 2: left, 3: up, 4: down, 5: 90 deg NW, 6: 90 deg WN, 7: 90 deg NE
# 8: 90 deg EN, 9: 90 deg SE, 10: 90 deg ES ,11: 90 deg SW, 12: 90 deg WS, -1:
path = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 6, 3, 11, 2, 8, 3,
        9, 1, 6, 3, 9, 1, 12, 4, 7, 1, 12, 4,
        5, 2, 10, 4, 7, 1, 1, 1, 1, 1, 1, 1, 1 -1]
B_particles = []
R_particles = []
# Colors -------------------------------------------------------------- #
Color_Yellow = (255, 255, 102)
Color_Red = (255, 51, 51)
Color_Dark_Red = (153, 0, 0)
Color_Blue = (51, 153, 255)
Color_Dark_Blue = (0, 76, 153)
Color_Light_Green = (102, 255, 178)
Color_Purple = (255, 51, 153)
Color_Black = (0, 0, 0)
Color_White = (255, 255, 255)
# loop  -------------------------------------------------------------------------------------------------------------------------------------------------------- #
while (1):
    screen.fill((0+Background_color_decay, 25, 51))
    # reference plane -------------------------------------------------------------- #
    if gamerule_show_reference_axis == True:
        pg.draw.line(screen, Color_Purple, (win_x/2, 0), (win_x/2, win_y))
        pg.draw.line(screen, Color_Purple, (0, win_y/2), (win_x, win_y/2))
        pg.draw.line(screen, Color_Light_Green, (refX, 0), (refX, win_y))
        pg.draw.line(screen, Color_Light_Green, (0, refY), (win_x, refY))
    # blue particle -------------------------------------------------------------- #
    B_particles.append(
        [[refX+posX_B, refY+posY_B], [0, 0], r.randint(10, 20)])
    for particle in B_particles:
        particle[0][0] += particle[1][0]
        particle[0][1] += particle[1][1]
        # decay -------------------------------------------------------------- #
        particle[2] -= 0.15
        # generator -------------------------------------------------------------- #
        if Center_B == 100:
            pg.draw.circle(screen, Color_Dark_Blue, [
                int(particle[0][0]), int(particle[0][1])], int(particle[2]))
            if particle[2] <= 0:
                B_particles.remove(particle)  # might have glitch
    # red particle -------------------------------------------------------------- #
    R_particles.append(
        [[refX+posX_R, refY+posY_R], [0, 0], r.randint(10, 20)])
    for particle in R_particles:
        particle[0][0] += particle[1][0]
        particle[0][1] += particle[1][1]
        # decay -------------------------------------------------------------- #
        particle[2] -= 0.15
        # generator -------------------------------------------------------------- #
        if Center_R == 100:
            pg.draw.circle(screen, Color_Dark_Red, [
                int(particle[0][0]), int(particle[0][1])], int(particle[2]))
            if particle[2] <= 0:
                R_particles.remove(particle)  # might have glitch
    # stabilizer -------------------------------------------------------------- # Slowly bring reference plane back to middle
    if refY > win_y/2:
        refY -= 1/2
    if refY < win_y/2:
        refY += 1/2
    if refX > win_x/2:
        refX -= 1/2
    if refX < win_x/2:
        refX += 1/2
    # time loop as degree -------------------------------------------------------------- #
    if deg >= 360:  # uses >= for safety
        deg = 0
    deg += 0.8
    pg.time.delay(1)  # 1 millisecond
    # path 1,2 (horizontal movement) -------------------------------------------------------------- # has to be in while loop since position has to be updated.
    path_horizon_length = 100
    path_horizon_height = 50
    path_horizon_posX = refX-(path_horizon_length/2)
    path_horizon_posY = refY-(path_horizon_height/2)
    # path 3,4 (vertical movement)
    path_vert_length = 50
    path_vert_height = 100
    path_vert_posX = refX-(path_vert_length/2)
    path_vert_posY = refY-(path_vert_height/2)
    # path 5,6 (90 degree NW)
    (path_NW_1_posX, path_NW_1_posY) = (refX-50, refY+23)
    (path_NW_2_posX, path_NW_2_posY) = (refX+23, refY+23)
    (path_NW_3_posX, path_NW_3_posY) = (refX+23, refY-50)
    (path_NW_4_posX, path_NW_4_posY) = (refX-25, refY-50)
    (path_NW_5_posX, path_NW_5_posY) = (refX-25, refY-25)
    (path_NW_6_posX, path_NW_6_posY) = (refX-50, refY-25)
    # path 7,8 (90 degree NE)
    (path_NE_1_posX, path_NE_1_posY) = (refX+50, refY+23)
    (path_NE_2_posX, path_NE_2_posY) = (refX+50, refY-25)
    (path_NE_3_posX, path_NE_3_posY) = (refX+23, refY-25)
    (path_NE_4_posX, path_NE_4_posY) = (refX+23, refY-50)
    (path_NE_5_posX, path_NE_5_posY) = (refX-25, refY-50)
    (path_NE_6_posX, path_NE_6_posY) = (refX-25, refY+23)
    # path 9,10 (90 degree SE)
    (path_SE_1_posX, path_SE_1_posY) = (refX+23, refY+50)
    (path_SE_2_posX, path_SE_2_posY) = (refX+23, refY+23)
    (path_SE_3_posX, path_SE_3_posY) = (refX+50, refY+23)
    (path_SE_4_posX, path_SE_4_posY) = (refX+50, refY-25)
    (path_SE_5_posX, path_SE_5_posY) = (refX-25, refY-25)
    (path_SE_6_posX, path_SE_6_posY) = (refX-25, refY+50)
    # path 11,12 (90 degree SW)
    (path_SW_1_posX, path_SW_1_posY) = (refX+23, refY+50)
    (path_SW_2_posX, path_SW_2_posY) = (refX+23, refY-25)
    (path_SW_3_posX, path_SW_3_posY) = (refX-50, refY-25)
    (path_SW_4_posX, path_SW_4_posY) = (refX-50, refY+23)
    (path_SW_5_posX, path_SW_5_posY) = (refX-25, refY+23)
    (path_SW_6_posX, path_SW_6_posY) = (refX-25, refY+50)
    # path generation -------------------------------------------------------------- #
    i = 0
    j = 0
    for k in range(len(path)):
        if path[k] == 0:
            pg.draw.rect(screen, Color_White, (path_horizon_posX+(i*100)-cx,
                         path_horizon_posY-(j*100)-cy, path_horizon_length, path_horizon_height), 2)
            i += 1  # axis increment
        elif path[k] == -1:
            pg.draw.rect(screen, Color_Dark_Red, (path_horizon_posX+(i*100)-cx,
                         path_horizon_posY-(j*100)-cy, path_horizon_length, path_horizon_height), 2)
        elif path[k] == 1:
            pg.draw.rect(screen, Color_Yellow, (path_horizon_posX+(i*100)-cx,
                         path_horizon_posY-(j*100)-cy, path_horizon_length, path_horizon_height), 2)
            i += 1  # axis increment
        elif path[k] == 2:
            pg.draw.rect(screen, Color_Yellow, (path_horizon_posX+(i*100)-cx,
                         path_horizon_posY-(j*100)-cy, path_horizon_length, path_horizon_height), 2)
            i -= 1  # axis increment
        elif path[k] == 3:
            pg.draw.rect(screen, Color_Yellow, (path_vert_posX+(i*100)-cx,
                         path_vert_posY-(j*100)-cy, path_vert_length, path_vert_height), 2)
            j += 1  # axis increment
        elif path[k] == 4:
            pg.draw.rect(screen, Color_Yellow, (path_vert_posX+(i*100)-cx,
                         path_vert_posY-(j*100)-cy, path_vert_length, path_vert_height), 2)
            j -= 1  # axis increment
        elif path[k] == 5 or path[k] == 6:
            pg.draw.polygon(screen, Color_Yellow,
                            ((path_NW_1_posX+(i*100)-cx,
                              path_NW_1_posY-(j*100)-cy),
                             (path_NW_2_posX+(i*100)-cx,
                              path_NW_2_posY-(j*100)-cy),
                             (path_NW_3_posX+(i*100)-cx,
                              path_NW_3_posY-(j*100)-cy),
                             (path_NW_4_posX+(i*100)-cx,
                              path_NW_4_posY-(j*100)-cy),
                             (path_NW_5_posX+(i*100)-cx,
                              path_NW_5_posY-(j*100)-cy),
                             (path_NW_6_posX+(i*100)-cx,
                              path_NW_6_posY-(j*100)-cy)), 2)
            if path[k] == 5:
                i -= 1  # axis increment
            elif path[k] == 6:
                j += 1  # axis increment
        elif path[k] == 7 or path[k] == 8:
            pg.draw.polygon(screen, Color_Yellow,
                            ((path_NE_1_posX+(i*100)-cx,
                              path_NE_1_posY-(j*100)-cy),
                             (path_NE_2_posX+(i*100)-cx,
                              path_NE_2_posY-(j*100)-cy),
                             (path_NE_3_posX+(i*100)-cx,
                              path_NE_3_posY-(j*100)-cy),
                             (path_NE_4_posX+(i*100)-cx,
                              path_NE_4_posY-(j*100)-cy),
                             (path_NE_5_posX+(i*100)-cx,
                              path_NE_5_posY-(j*100)-cy),
                             (path_NE_6_posX+(i*100)-cx,
                              path_NE_6_posY-(j*100)-cy)), 2)
            if path[k] == 7:
                i += 1  # axis increment
            elif path[k] == 8:
                j += 1  # axis increment
        elif path[k] == 9 or path[k] == 10:
            pg.draw.polygon(screen, Color_Yellow,
                            ((path_SE_1_posX+(i*100)-cx,
                              path_SE_1_posY-(j*100)-cy),
                             (path_SE_2_posX+(i*100)-cx,
                              path_SE_2_posY-(j*100)-cy),
                             (path_SE_3_posX+(i*100)-cx,
                              path_SE_3_posY-(j*100)-cy),
                             (path_SE_4_posX+(i*100)-cx,
                              path_SE_4_posY-(j*100)-cy),
                             (path_SE_5_posX+(i*100)-cx,
                              path_SE_5_posY-(j*100)-cy),
                             (path_SE_6_posX+(i*100)-cx,
                              path_SE_6_posY-(j*100)-cy)), 2)
            if path[k] == 9:
                i += 1  # axis increment
            elif path[k] == 10:
                j -= 1  # axis increment
        elif path[k] == 11 or path[k] == 12:
            pg.draw.polygon(screen, Color_Yellow,
                            ((path_SW_1_posX+(i*100)-cx,
                              path_SW_1_posY-(j*100)-cy),
                             (path_SW_2_posX+(i*100)-cx,
                              path_SW_2_posY-(j*100)-cy),
                             (path_SW_3_posX+(i*100)-cx,
                              path_SW_3_posY-(j*100)-cy),
                             (path_SW_4_posX+(i*100)-cx,
                              path_SW_4_posY-(j*100)-cy),
                             (path_SW_5_posX+(i*100)-cx,
                              path_SW_5_posY-(j*100)-cy),
                             (path_SW_6_posX+(i*100)-cx,
                              path_SW_6_posY-(j*100)-cy)), 2)
            if path[k] == 11:
                i -= 1  # axis increment
            if path[k] == 12:
                j -= 1  # axis increment
    # coloration
    if Background_color_decay != 0:
        Background_color_decay -= 1
        # circles -------------------------------------------------------------- #
    pg.draw.circle(screen, Color_Blue, (refX+posX_B, refY+posY_B), 20)
    pg.draw.circle(screen, Color_Red, (refX+posX_R, refY+posY_R), 20)

    # wave-based time loop -------------------------------------------------------------- #
    posX_B = Center_B*(m.sin(m.radians(-deg)))
    posY_B = Center_B*(m.cos(m.radians(-deg)))
    posX_R = Center_R*(m.sin(m.radians(-deg+180)))
    posY_R = Center_R*(m.cos(m.radians(-deg+180)))
    pg.display.update()
    # event  ------------------------------------------------------------------------------------------------------------------------------------------------ #
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        # keyboard pressed -------------------------------------------------------------- #
        if event.type == pg.KEYDOWN:
            # Blue -------------------------------------------------------------- # (deg 0)
            if Center_B == 100:
                # path movement -------------------------------------------------------------- #
                if path[path_position] == 0:
                    if 225 < deg < 315:
                        cx += 100
                        path_position += 1
                        (Center_B, Center_R) = 0, 100
                        refX = refX+posX_B
                    else:
                        Background_color_decay = 150
                elif path[path_position] == -1:
                    if 45 < deg < 135:
                        cx -= 100
                        path_position -= 1
                        (Center_B, Center_R) = 0, 100
                        refX = refX+posX_B
                    else:
                        Background_color_decay = 150
                elif path[path_position] == 1:
                    if 45 < deg < 135:
                        cx -= 100
                        path_position -= 1
                        (Center_B, Center_R) = 0, 100
                        refX = refX+posX_B
                    elif 225 < deg < 315:
                        cx += 100
                        path_position += 1
                        (Center_B, Center_R) = 0, 100
                        refX = refX+posX_B
                    else:
                        Background_color_decay = 150
                elif path[path_position] == 2:
                    if 45 < deg < 135:
                        cx -= 100
                        path_position += 1
                        (Center_B, Center_R) = 0, 100
                        refX = refX+posX_B
                    elif 225 < deg < 315:
                        cx += 100
                        path_position -= 1
                        (Center_B, Center_R) = 0, 100
                        refX = refX+posX_B
                    else:
                        Background_color_decay = 150
                elif path[path_position] == 3:
                    if 135 < deg < 225:
                        cy -= 100
                        path_position += 1
                        (Center_B, Center_R) = 0, 100
                        refY = refY+posY_B
                    elif 0 <= deg < 45 or 315 < deg <= 360:
                        cy += 100
                        path_position -= 1
                        (Center_B, Center_R) = 0, 100
                        refY = refY+posY_B
                    else:
                        Background_color_decay = 150
                elif path[path_position] == 4:
                    if 135 < deg <= 225:
                        cy -= 100
                        path_position -= 1
                        (Center_B, Center_R) = 0, 100
                        refY = refY+posY_B
                    elif 0 <= deg < 45 or 315 < deg <= 360:
                        cy += 100
                        path_position += 1
                        (Center_B, Center_R) = 0, 100
                        refY = refY+posY_B
                    else:
                        Background_color_decay = 150
                elif path[path_position] == 5:
                    if 135 < deg < 225:
                        cy -= 100
                        path_position -= 1
                        (Center_B, Center_R) = 0, 100
                        refY = refY+posY_B
                    elif 45 < deg < 135:
                        cx -= 100
                        path_position += 1
                        (Center_B, Center_R) = 0, 100
                        refX = refX+posX_B
                    else:
                        Background_color_decay = 150
                elif path[path_position] == 6:
                    if 135 < deg < 225:
                        cy -= 100
                        path_position += 1
                        (Center_B, Center_R) = 0, 100
                        refY = refY+posY_B
                    elif 45 < deg < 135:
                        cx -= 100
                        path_position -= 1
                        (Center_B, Center_R) = 0, 100
                        refX = refX+posX_B
                    else:
                        Background_color_decay = 150
                elif path[path_position] == 7:
                    if 135 < deg < 225:
                        cy -= 100
                        path_position -= 1
                        (Center_B, Center_R) = 0, 100
                        refY = refY+posY_B
                    elif 225 < deg < 315:
                        cx += 100
                        path_position += 1
                        (Center_B, Center_R) = 0, 100
                        refX = refX+posX_B
                    else:
                        Background_color_decay = 150
                elif path[path_position] == 8:
                    if 135 < deg < 225:
                        cy -= 100
                        path_position += 1
                        (Center_B, Center_R) = 0, 100
                        refY = refY+posY_B
                    elif 225 < deg < 315:
                        cx += 100
                        path_position -= 1
                        (Center_B, Center_R) = 0, 100
                        refX = refX+posX_B
                    else:
                        Background_color_decay = 150
                elif path[path_position] == 9:
                    if 0 <= deg < 45 or 315 < deg <= 360:
                        cy += 100
                        path_position -= 1
                        (Center_B, Center_R) = 0, 100
                        refY = refY+posY_B
                    elif 225 < deg < 315:
                        cx += 100
                        path_position += 1
                        (Center_B, Center_R) = 0, 100
                        refX = refX+posX_B
                    else:
                        Background_color_decay = 150
                elif path[path_position] == 10:
                    if 0 <= deg < 45 or 315 < deg <= 360:
                        cy += 100
                        path_position += 1
                        (Center_B, Center_R) = 0, 100
                        refY = refY+posY_B
                    elif 225 < deg < 315:
                        cx += 100
                        path_position -= 1
                        (Center_B, Center_R) = 0, 100
                        refX = refX+posX_B
                    else:
                        Background_color_decay = 150
                elif path[path_position] == 11:
                    if 45 < deg < 135:
                        cx -= 100
                        path_position += 1
                        (Center_B, Center_R) = 0, 100
                        refX = refX+posX_B
                    elif 0 <= deg <= 45 or 315 < deg <= 360:
                        cy += 100
                        path_position -= 1
                        (Center_B, Center_R) = 0, 100
                        refY = refY+posY_B
                    else:
                        Background_color_decay = 150
                elif path[path_position] == 12:
                    if 45 < deg < 135:
                        cx -= 100
                        path_position -= 1
                        (Center_B, Center_R) = 0, 100
                        refX = refX+posX_B
                    elif 0 <= deg <= 45 or 315 < deg <= 360:
                        cy += 100
                        path_position += 1
                        (Center_B, Center_R) = 0, 100
                        refY = refY+posY_B
                    else:
                        Background_color_decay = 150
            # Red -------------------------------------------------------------- # (deg +180)
            elif Center_R == 100:
                # path movement -------------------------------------------------------------- #
                if path[path_position] == 0:
                    if 45 < deg < 135:
                        cx += 100
                        path_position += 1
                        (Center_B, Center_R) = 100, 0
                        refX = refX+posX_R
                    else:
                        Background_color_decay = 150
                elif path[path_position] == -1:
                    if 225 < deg < 315:
                        cx -= 100
                        path_position -= 1
                        (Center_B, Center_R) = 100, 0
                        refX = refX+posX_R
                    else:
                        Background_color_decay = 150
                elif path[path_position] == 1:
                    if 45 < deg < 135:
                        cx += 100
                        path_position += 1
                        (Center_B, Center_R) = 100, 0
                        refX = refX+posX_R
                    elif 225 < deg < 315:
                        cx -= 100
                        path_position -= 1
                        (Center_B, Center_R) = 100, 0
                        refX = refX+posX_R
                    else:
                        Background_color_decay = 150
                elif path[path_position] == 2:
                    if 45 < deg <= 135:
                        cx += 100
                        path_position -= 1
                        (Center_B, Center_R) = 100, 0
                        refX = refX+posX_R
                    elif 225 < deg <= 315:
                        cx -= 100
                        path_position += 1
                        (Center_B, Center_R) = 100, 0
                        refX = refX+posX_R
                    else:
                        Background_color_decay = 150
                elif path[path_position] == 3:
                    if 135 < deg < 225:
                        cy += 100
                        path_position -= 1
                        (Center_B, Center_R) = 100, 0
                        refY = refY+posY_R
                    elif 0 <= deg < 45 or 315 < deg <= 360:
                        cy -= 100
                        path_position += 1
                        (Center_B, Center_R) = 100, 0
                        refY = refY+posY_R
                    else:
                        Background_color_decay = 150
                elif path[path_position] == 4:
                    if 135 < deg < 225:
                        cy += 100
                        path_position += 1
                        (Center_B, Center_R) = 100, 0
                        refY = refY+posY_R
                    elif 0 <= deg < 45 or 315 < deg <= 360:
                        cy -= 100
                        path_position -= 1
                        (Center_B, Center_R) = 100, 0
                        refY = refY+posY_R
                    else:
                        Background_color_decay = 150
                elif path[path_position] == 5:
                    if 0 < deg < 45 or 315 < deg <= 360:
                        cy -= 100
                        path_position -= 1
                        (Center_B, Center_R) = 100, 0
                        refY = refY+posY_R
                    elif 225 < deg < 315:
                        cx -= 100
                        path_position += 1
                        (Center_B, Center_R) = 100, 0
                        refX = refX+posX_R
                    else:
                        Background_color_decay = 150
                elif path[path_position] == 6:
                    if 0 < deg < 45 or 315 < deg <= 360:
                        cy -= 100
                        path_position += 1
                        (Center_B, Center_R) = 100, 0
                        refY = refY+posY_R
                    elif 225 < deg < 315:
                        cx -= 100
                        path_position -= 1
                        (Center_B, Center_R) = 100, 0
                        refX = refX+posX_R
                    else:
                        Background_color_decay = 150
                elif path[path_position] == 7:
                    if 0 < deg < 45 or 315 < deg <= 360:
                        cy -= 100
                        path_position -= 1
                        (Center_B, Center_R) = 100, 0
                        refY = refY+posY_R
                    elif 45 < deg < 135:
                        cx += 100
                        path_position += 1
                        (Center_B, Center_R) = 100, 0
                        refX = refX+posX_R
                    else:
                        Background_color_decay = 150
                elif path[path_position] == 8:
                    if 0 < deg < 45 or 315 < deg <= 360:
                        cy -= 100
                        path_position += 1
                        (Center_B, Center_R) = 100, 0
                        refY = refY+posY_R
                    elif 45 < deg < 135:
                        cx += 100
                        path_position -= 1
                        (Center_B, Center_R) = 100, 0
                        refX = refX+posX_R
                    else:
                        Background_color_decay = 150
                elif path[path_position] == 9:
                    if 135 < deg < 225:
                        cy += 100
                        path_position -= 1
                        (Center_B, Center_R) = 100, 0
                        refY = refY+posY_R
                    elif 45 < deg <= 135:
                        cx += 100
                        path_position += 1
                        (Center_B, Center_R) = 100, 0
                        refX = refX+posX_R
                    else:
                        Background_color_decay = 150
                elif path[path_position] == 10:
                    if 135 < deg < 225:
                        cy += 100
                        path_position += 1
                        (Center_B, Center_R) = 100, 0
                        refY = refY+posY_R
                    elif 45 < deg <= 135:
                        cx += 100
                        path_position -= 1
                        (Center_B, Center_R) = 100, 0
                        refX = refX+posX_R
                    else:
                        Background_color_decay = 150
                elif path[path_position] == 11:
                    if 135 < deg <= 225:
                        cy += 100
                        path_position -= 1
                        (Center_B, Center_R) = 100, 0
                        refY = refY+posY_R
                    elif 225 < deg <= 315:
                        cx -= 100
                        path_position += 1
                        (Center_B, Center_R) = 100, 0
                        refX = refX+posX_R
                    else:
                        Background_color_decay = 150
                elif path[path_position] == 12:
                    if 135 < deg <= 225:
                        cy += 100
                        path_position += 1
                        (Center_B, Center_R) = 100, 0
                        refY = refY+posY_R
                    elif 225 < deg <= 315:
                        cx -= 100
                        path_position -= 1
                        (Center_B, Center_R) = 100, 0
                        refX = refX+posX_R
                    else:
                        Background_color_decay = 150
