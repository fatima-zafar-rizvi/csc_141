import pygame
import sys

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
GRID_ROWS = 5  # Number of rows in the grid
GRID_COLS = 7  # Number of columns in the grid

try:
    star_image = pygame.image.load('images/star.png')  
    star_image = pygame.transform.scale(star_image, (STAR_WIDTH, STAR_HEIGHT)) 
except pygame.error as e:
    print(f"Error loading star image: {e}")
    sys.exit()

# Calculate grid dimensions and positioning
grid_width = GRID_COLS * STAR_WIDTH
grid_height = GRID_ROWS * STAR_HEIGHT
grid_start_x = (SCREEN_WIDTH - grid_width) // 2
grid_start_y = (SCREEN_HEIGHT - grid_height) // 2

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Centered Star Grid")

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Draw background
    screen.fill(BLACK)

    # Draw stars in a centered grid
    for row in range(GRID_ROWS):
        for col in range(GRID_COLS):
            x = grid_start_x + col * STAR_WIDTH
            y = grid_start_y + row * STAR_HEIGHT
            screen.blit(star_image, (x, y))

    # Update the display
    pygame.display.flip()
