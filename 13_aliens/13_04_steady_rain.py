import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
BLACK = (0, 0, 0)

# Raindrop settings
RAINDROP_WIDTH = 30
RAINDROP_HEIGHT = 30
GRID_ROWS = 5
GRID_COLS = 10
RAINDROP_SPEED = 5

try:
    raindrop_image = pygame.image.load('images/raindrop.png')  
    raindrop_image = pygame.transform.scale(raindrop_image, (RAINDROP_WIDTH, 
                                                             RAINDROP_HEIGHT))  
except pygame.error as e:
    print(f"Error loading raindrop image: {e}")
    sys.exit()

# Create a grid of raindrops
def create_raindrops():
    return [
        {"x": col * (RAINDROP_WIDTH + 20),
          "y": row * (RAINDROP_HEIGHT + 20) - SCREEN_HEIGHT}
        for row in range(GRID_ROWS)
        for col in range(GRID_COLS)
    ]

raindrops = create_raindrops()

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Falling Raindrops with Delayed Row Reset")

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update raindrop positions
    all_off_screen = True
    for raindrop in raindrops:
        raindrop["y"] += RAINDROP_SPEED
        if raindrop["y"] < SCREEN_HEIGHT:
            all_off_screen = False

    # If all raindrops are off-screen, reset the grid
    if all_off_screen:
        raindrops = create_raindrops()

    # Draw background
    screen.fill(BLACK)

    # Draw raindrops
    for raindrop in raindrops:
        screen.blit(raindrop_image, (raindrop["x"], raindrop["y"]))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)