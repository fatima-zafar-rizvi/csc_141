import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
BLUE = (0, 0, 255)

# Rocket settings
ROCKET_WIDTH = 50
ROCKET_HEIGHT = 50
try:
    rocket_image = pygame.image.load('images/rocket.png')
    rocket_image = pygame.transform.scale(rocket_image, (ROCKET_WIDTH, 
                                                         ROCKET_HEIGHT))  
except pygame.error as e:
    print(f"Error loading rocket image: {e}")
    sys.exit()

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Rocket Game")

# Rocket starting position
rocket_x = (SCREEN_WIDTH - ROCKET_WIDTH) // 2
rocket_y = (SCREEN_HEIGHT - ROCKET_HEIGHT) // 2

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get keys pressed
    keys = pygame.key.get_pressed()

    # Move rocket based on key input
    if keys[pygame.K_UP]:
        rocket_y = max(0, rocket_y - 5)  # Ensure it doesn't go beyond top
    if keys[pygame.K_DOWN]:
        rocket_y = min(SCREEN_HEIGHT - ROCKET_HEIGHT, rocket_y + 5)  # Bottom
    if keys[pygame.K_LEFT]:
        rocket_x = max(0, rocket_x - 5)  # Left
    if keys[pygame.K_RIGHT]:
        rocket_x = min(SCREEN_WIDTH - ROCKET_WIDTH, rocket_x + 5)  # Right

    # Draw everything
    screen.fill(BLUE)  # Clear the screen
    screen.blit(rocket_image, (rocket_x, rocket_y))  # Draw the rocket image

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)
