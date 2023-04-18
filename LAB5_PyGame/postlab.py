import pygame
import math

pygame.init()

# set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# set up the clock
clock = pygame.time.Clock()

# define the colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# define the projectile
class Projectile:
    def __init__(self, x, y, angle, velocity):
        self.x = x
        self.y = y
        self.angle = angle
        self.velocity = velocity
        self.gravity = 9.8
        self.time = 0
        self.radius = 10

    def update(self):
        self.time += 0.1
        self.x = int(self.x + self.velocity * math.cos(self.angle) * self.time)
        self.y = int(self.y - self.velocity * math.sin(self.angle) * self.time + 0.5 * self.gravity * self.time**2)

    def draw(self):
        pygame.draw.circle(screen, red, (self.x, self.y), self.radius)

# create a list of projectiles
projectiles = []

# main game loop
running = True
while running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # clear the screen
    screen.fill(white)

    # update and draw the projectiles
    for projectile in projectiles:
        projectile.update()
        projectile.draw()

    # add a new projectile when the mouse is clicked
    if pygame.mouse.get_pressed()[0]:
        x, y = pygame.mouse.get_pos()
        angle = math.atan2(screen_height - y, x)
        velocity = 20
        projectile = Projectile(0, screen_height, angle, velocity)
        projectiles.append(projectile)

    # update the display
    pygame.display.update()

    # set the frame rate
    clock.tick(120)

# quit the game
pygame.quit()
