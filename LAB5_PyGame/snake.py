import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Define the game window dimensions
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 640
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the game window title
pygame.display.set_caption("Galaga")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Create the player sprite
player_width, player_height = 32, 32
player_x = SCREEN_WIDTH // 2 - player_width // 2
player_y = SCREEN_HEIGHT - player_height
player_speed = 5
player_rect = pygame.Rect(player_x, player_y, player_width, player_height)

# Create the enemy sprites
enemy_rows = 4
enemy_cols = 10
enemy_width, enemy_height = 32, 32
enemy_positions = []
for row in range(enemy_rows):
    for col in range(enemy_cols):
        enemy_x = col * enemy_width + 50
        enemy_y = row * enemy_height + 50
        enemy_positions.append((enemy_x, enemy_y))
enemy_sprites = [pygame.Rect(*pos, enemy_width, enemy_height) for pos in enemy_positions]

# Define the enemy triangle vertices
enemy_vertices = [(0, 0), (16, 32), (32, 0)]

# Set up the clock
clock = pygame.time.Clock()

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    # Handle player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    elif keys[pygame.K_RIGHT] and player_x + player_width < SCREEN_WIDTH:
        player_x += player_speed
    player_rect.x, player_rect.y = player_x, player_y
    
    # Move the enemy sprites
    for enemy_sprite in enemy_sprites:
        enemy_sprite.move_ip(0, 2)
    
    # Draw the game window
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, player_rect)
    for enemy_sprite in enemy_sprites:
        # Calculate the rotation angle based on the enemy's position
        dx = enemy_sprite.centerx - player_x
        dy = enemy_sprite.centery - player_y
        angle = math.degrees(math.atan2(dy, dx))
        # Calculate the rotated triangle vertices
        rotated_vertices = []
        for vertex in enemy_vertices:
            x, y = vertex
            x = x - enemy_width / 2
            y = y - enemy_height / 2
            x, y = (
                x * math.cos(math.radians(angle)) - y * math.sin(math.radians(angle)),
                x * math.sin(math.radians(angle)) + y * math.cos(math.radians(angle))
            )
            x, y = x + enemy_width / 2, y + enemy_height / 2
            x, y = x + enemy_sprite.x, y + enemy_sprite.y
            rotated_vertices.append((x, y))
        # Draw the rotated triangle
        pygame.draw.polygon(screen, RED, rotated_vertices)
    
    # Update the display
    pygame.display.update()
    
    # Set the frame rate
    clock.tick(60)
