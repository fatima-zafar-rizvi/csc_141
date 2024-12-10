import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Ship settings
SHIP_WIDTH = 50
SHIP_HEIGHT = 50
try:
    ship_image = pygame.image.load('images/rocket.png')
    ship_image = pygame.transform.scale(ship_image, (SHIP_WIDTH, SHIP_HEIGHT)) 
    ship_image = pygame.transform.rotate(ship_image, -90) # Rotate the image 
except pygame.error as e:
    print(f"Error loading ship image: {e}")
    sys.exit()

# Bullet settings
BULLET_WIDTH = 10
BULLET_HEIGHT = 5
BULLET_COLOR = RED
BULLET_SPEED = 7

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sideways Shooter")

# Ship starting position
ship_x = 50
ship_y = (SCREEN_HEIGHT - SHIP_HEIGHT) // 2

# Bullet list
bullets = []

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Create a new bullet
                bullet_x = ship_x + SHIP_WIDTH
                bullet_y = ship_y + SHIP_HEIGHT // 2 - BULLET_HEIGHT // 2
                bullets.append(pygame.Rect(bullet_x, bullet_y, BULLET_WIDTH, 
                                           BULLET_HEIGHT))

    # Get keys pressed
    keys = pygame.key.get_pressed()

    # Move ship based on key input
    if keys[pygame.K_UP]:
        ship_y = max(0, ship_y - 5) 
    if keys[pygame.K_DOWN]:
        ship_y = min(SCREEN_HEIGHT - SHIP_HEIGHT, ship_y + 5) 

    # Move bullets
    for bullet in bullets:
        bullet.x += BULLET_SPEED

    # Remove bullets that are off-screen
    bullets = [bullet for bullet in bullets if bullet.x <= SCREEN_WIDTH]

    # Draw everything
    screen.fill(BLACK)  # Clear the screen
    screen.blit(ship_image, (ship_x, ship_y))  # Draw the ship
    for bullet in bullets:
        pygame.draw.rect(screen, BULLET_COLOR, bullet)  # Draw the bullets

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)
