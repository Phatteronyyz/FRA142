import sys
import pygame as pg

class Rectangle:
    def __init__(self,x=0,y=0,w=0,h=0):
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height
    def draw(self,screen):
        pg.draw.rect(screen,color,(self.x,self.y,self.w,self.h))

class Button(Rectangle):
    def __init__(self, x=0, y=0, w=0, h=0):
        Rectangle.__init__(self, x, y, w, h)
    
    def isMouseOn(self):
        mouseX, mouseY = pg.mouse.get_pos()
        if (mouseX >= self.x and mouseX <= self.x+self.w and mouseY >= self.y and mouseY <= self.y+self.h):
            return True
        else:
            return False
        
    def isMousePress(self):
        if pg.mouse.get_pressed()[0]:
            return True
        else:
            return False

class InputBox:

    def __init__(self, x, y, w, h, canAlpha, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False
        self.canalpha = canAlpha

    def handle_event(self, event):
        
        if event.type == pg.MOUSEBUTTONDOWN:# ทำการเช็คว่ามีการคลิก Mouse หรือไม่
            if self.rect.collidepoint(event.pos): #ทำการเช็คว่าตำแหน่งของ Mouse อยู่บน InputBox นี้หรือไม่
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE # เปลี่ยนสีของ InputBox
            
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    if self.canalpha:
                        self.text += event.unicode
                    elif not self.canalpha:
                        if chr(event.key).isnumeric():
                            self.text += event.unicode

                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, Screen):
        # Blit the text.
        Screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(Screen, self.color, self.rect, 2)

pg.init()
win_x, win_y = 800, 600
screen = pg.display.set_mode((win_x, win_y))

COLOR_INACTIVE = pg.Color('lightskyblue3') # ตั้งตัวแปรให้เก็บค่าสี เพื่อนำไปใช้เติมสีให้กับกล่องข้อความตอนที่คลิกที่กล่องนั้นๆอยู่
COLOR_ACTIVE = pg.Color('dodgerblue2')     # ^^^
FONT = pg.font.Font(None, 32)

input_box1 = InputBox(350, 65, 140, 32, True) # สร้าง InputBox1
input_box2 = InputBox(350, 165, 140, 32, True) # สร้าง InputBox2
input_box3 = InputBox(295, 265, 140, 32, False) # สร้าง InputBox3
input_boxes = [input_box1, input_box2, input_box3] # เก็บ InputBox ไว้ใน list เพื่อที่จะสามารถนำไปเรียกใช้ได้ง่าย
btn = Button(70,350,100,30)
run = True

font = pg.font.Font('Kanit-Regular.ttf', 20) # font and fontsize
text = font.render('', True, (11,36,71)) # (text,is smooth?,letter color,background color)
textRect = text.get_rect() # text size
firstnametext = font.render('Please input your first name :', True, (0,0,0))
firsttextRect = firstnametext.get_rect()
lastnametext = font.render('Please input your last name :', True, (0,0,0))
lasttextRect = firstnametext.get_rect()
agetext = font.render('Please input your age :', True, (0,0,0))
ageRect = firstnametext.get_rect()
submittext = font.render('SUBMIT', True, (255,255,255))
submitRect = firstnametext.get_rect()
isnumbertext = font.render('Please input number', True, (0,255,255))
isnumberRect = firstnametext.get_rect()
showtext = False

firsttextRect.center = (200,80)
lasttextRect.center = (200,180)
ageRect.center = (200,280)
submitRect.center = (217,365)
textRect.center = (70, 450)
isnumberRect.center = (200, 200)

showerror = False

while run:
    screen.fill((255, 255, 255))

    screen.blit(firstnametext, firsttextRect)
    screen.blit(lastnametext, lasttextRect)
    screen.blit(agetext, ageRect)

    for box in input_boxes: # ทำการเรียก InputBox ทุกๆตัว โดยการ Loop เข้าไปยัง list ที่เราเก็บค่า InputBox ไว้
        box.update() # เรียกใช้ฟังก์ชัน update() ของ InputBox
        box.draw(screen) # เรียกใช้ฟังก์ชัน draw() ของ InputBox เพื่อทำการสร้างรูปบน Screen

    if btn.isMouseOn() and btn.isMousePress():
        text = font.render('Hello ' + input_box1.text + ' ' + input_box2.text + '! You are ' + input_box3.text + ' years old.', True, (11,36,71))
        showtext = True
        color = (165, 212, 232)
    elif btn.isMouseOn():
        color = (87, 108, 188)
    else:
        color = (25, 55, 109)

    btn.draw(screen)
    screen.blit(submittext, submitRect)

    if showtext:
        screen.blit(text, textRect)

    if showerror:
        print("wasd")
        screen.blit(isnumbertext, isnumberRect)
        
    for event in pg.event.get():
        for box in input_boxes:
            box.handle_event(event)
        if event.type == pg.QUIT:
            pg.quit()
            run = False

    pg.time.delay(1)
    pg.display.update()