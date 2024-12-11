import pygame
import sys
from random import randint, choice

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
BLACK = (0, 0, 0)

# Star settings
STAR_WIDTH = 50
STAR_HEIGHT = 50
NUM_STARS = 50  # Number of stars
MAX_SPEED = 3  # Maximum movement speed

try:
    star_image = pygame.image.load('images/star.png')  
    star_image = pygame.transform.scale(star_image, (STAR_WIDTH, STAR_HEIGHT))  
except pygame.error as e:
    print(f"Error loading star image: {e}")
    sys.exit()

# Generate random initial positions and speeds for the stars
stars = [
    {
        "x": randint(0, SCREEN_WIDTH - STAR_WIDTH),
        "y": randint(0, SCREEN_HEIGHT - STAR_HEIGHT),
        "speed": choice([-1, 1]) * randint(1, MAX_SPEED)
    }
    for _ in range(NUM_STARS)
]

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Moving Random Stars")

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update star positions
    for star in stars:
        star["x"] += star["speed"]
        # Reverse direction if the star moves out of bounds
        if star["x"] < 0 or star["x"] > SCREEN_WIDTH - STAR_WIDTH:
            star["speed"] *= -1

    # Draw background
    screen.fill(BLACK)

    # Draw stars
    for star in stars:
        screen.blit(star_image, (star["x"], star["y"]))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)
