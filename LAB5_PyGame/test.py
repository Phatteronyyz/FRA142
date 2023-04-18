import pygame
import math

pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set up the initial position, velocity, and acceleration of the projectile
x = 0
y = screen_height - 50
velocity = 5.13
angle = 45
theta = math.radians(angle)
x_velocity = velocity * math.cos(theta)
y_velocity = -velocity * math.sin(theta)
acceleration = 9.81

# Set up the colors
white = (255, 255, 255)
black = (0, 0, 0)

# Set up the loop
running = True
start_time = pygame.time.get_ticks()
max_x = x
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Clear the screen
    screen.fill(white)
    
    # Calculate the elapsed time since the last frame
    current_time = pygame.time.get_ticks()
    elapsed_time = (current_time - start_time) / 1000.0
    
    # Update the position of the projectile
    x += x_velocity * elapsed_time
    y += y_velocity * elapsed_time
    y_velocity += acceleration * elapsed_time
    
    # Draw the projectile
    pygame.draw.circle(screen, black, (int(x), int(y)), 10)
    
    # Check if the projectile has hit the ground
    if y >= screen_height:
        running = False
    
    # Update the maximum x position
    if x > max_x:
        max_x = x
    
    # Update the display
    pygame.display.update()

# Calculate the maximum range in meters
conversion_factor = 0.01  # meters per pixel
max_range = max_x * conversion_factor

# Print the maximum range in meters
print(f"Maximum range: {max_range:.2f} meters")

# Quit Pygame
pygame.quit()
