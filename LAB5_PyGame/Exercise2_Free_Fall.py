import pygame as pg
pg.init()

win_x, win_y = 800, 900 #1 ขนาดหน้าจอ

screen = pg.display.set_mode((win_x, win_y)) #1 สร้างหน้าต่างเกม

posX, posY = 500, 90

time = 0

while(1): #2 ทำการสร้าง loop
    screen.fill((255, 255, 255)) #3ตั้งสีพื้นหลัง

    pg.draw.circle(screen,(102,178,255),(posX,posY),20)

    posY += 0.5 * 1 * (time**2)
        
    pg.time.delay(1) #หน่วงเวลา

    time += 0.001
    
    pg.display.update() #4 ทำการอัพเดท

    if(posY >= 900):
        # pg.quit()
        # exit()
        posY=900
    
    for event in pg.event.get(): # ทำการ Check event ต่างๆที่เกิดขึ้น
        if event.type == pg.QUIT: 
            pg.quit()
            exit()
