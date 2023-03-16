import pygame
import random

# Define constants
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
PADDLE_WIDTH = 20
PADDLE_HEIGHT = 140
BALL_SIZE = 10
PADDLE_SPEED = 5
BALL_SPEED = 5
BALL_ACCELERATION = 1.05
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT_SIZE = 36

# Initialize Pygame
pygame.init()
clock = pygame.time.Clock()

# Set up the window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pong")

# Set up the paddles
left_paddle = pygame.Rect(0, (WINDOW_HEIGHT - PADDLE_HEIGHT) // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = pygame.Rect(WINDOW_WIDTH - PADDLE_WIDTH, (WINDOW_HEIGHT - PADDLE_HEIGHT) // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Set up the ball
ball = pygame.Rect(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2, BALL_SIZE, BALL_SIZE)
ball_speed_x = BALL_SPEED * random.choice((1, -1))
ball_speed_y = BALL_SPEED * random.choice((1, -1))

# Set up the score counters
left_score = 0
right_score = 0
font = pygame.font.Font(None, FONT_SIZE)

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Move the paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        left_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_s]:
        left_paddle.y += PADDLE_SPEED
    if keys[pygame.K_UP]:
        right_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN]:
        right_paddle.y += PADDLE_SPEED

    # Move the ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Bounce the ball off the top and bottom walls
    if ball.top <= 0 or ball.bottom >= WINDOW_HEIGHT:
        ball_speed_y = -ball_speed_y

    # Check for a collision with the left paddle
    if ball.left <= left_paddle.right and ball.top >= left_paddle.top and ball.bottom <= left_paddle.bottom:
        ball_speed_x = BALL_SPEED
        ball_speed_y *= random.uniform(0.9, 1.1)
        ball_speed_y = -ball_speed_y

    # Check for a collision with the right paddle
    if ball.right >= right_paddle.left and ball.top >= right_paddle.top and ball.bottom <= right_paddle.bottom:
        ball_speed_x = -BALL_SPEED
        ball_speed_y *= random.uniform(0.9, 1.1)
        ball_speed_y = -ball_speed_y

    # Check for a point scored
    if ball.left <= 0:
        right_score += 1
        print("Right player scores!")
        ball_speed_x = BALL_SPEED
        ball_speed_y = BALL_SPEED * random.choice((1, -1))
        ball.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

    if ball.right >= WINDOW_WIDTH:
        left_score += 1
        print("Left player scores!")
        ball_speed_x = -BALL_SPEED
        ball_speed_y = BALL_SPEED * random.choice((1, -1))
        ball.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

    # Draw the game elements
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, left_paddle)
    pygame.draw.rect(screen, WHITE, right_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)

    # Draw the score counters
    left_score_text = font.render(str(left_score), True, WHITE)
    right_score_text = font.render(str(right_score), True, WHITE)
    screen.blit(left_score_text, (WINDOW_WIDTH // 4 - FONT_SIZE // 2, FONT_SIZE // 2))
    screen.blit(right_score_text, (WINDOW_WIDTH // 4 * 3 - FONT_SIZE // 2, FONT_SIZE // 2))

    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)

