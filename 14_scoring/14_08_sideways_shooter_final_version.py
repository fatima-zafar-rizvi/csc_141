import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Ship settings
SHIP_WIDTH = 50
SHIP_HEIGHT = 50
try:
    ship_image = pygame.image.load('images/rocket.png')
    ship_image = pygame.transform.scale(ship_image, (SHIP_WIDTH, SHIP_HEIGHT)) 
    ship_image = pygame.transform.rotate(ship_image, -90)  # Rotate the image 
except pygame.error as e:
    print(f"Error loading ship image: {e}")
    sys.exit()

# Bullet settings
BULLET_WIDTH = 10
BULLET_HEIGHT = 5
BULLET_COLOR = RED
BULLET_SPEED = 7

# Alien settings
ALIEN_WIDTH = 40
ALIEN_HEIGHT = 40
ALIEN_SPEED = 3
ALIEN_COLOR = (0, 255, 0)  # Green for aliens
aliens = []

# Load alien image
try:
    alien_image = pygame.image.load('images/alien.png')
    alien_image = pygame.transform.scale(alien_image, (ALIEN_WIDTH, ALIEN_HEIGHT))
except pygame.error as e:
    print(f"Error loading alien image: {e}")
    sys.exit()

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sideways Shooter")

# Ship starting position
ship_x = 50
ship_y = (SCREEN_HEIGHT - SHIP_HEIGHT) // 2

# Bullet list
bullets = []

# Game state variables
misses = 0
hits = 0
game_running = False

# Button settings
button_color = (0, 255, 0)
button_width = 200
button_height = 50
button_x = SCREEN_WIDTH // 2 - button_width // 2
button_y = SCREEN_HEIGHT // 2 - button_height // 2

# Create a Play button
def draw_play_button():
    font = pygame.font.Font(None, 36)
    button_text = font.render("Play", True, WHITE)
    pygame.draw.rect(screen, button_color, (button_x, button_y, button_width, button_height))
    screen.blit(button_text, (button_x + button_width // 2 - button_text.get_width() // 2,
                             button_y + button_height // 2 - button_text.get_height() // 2))

# Check if Play button is clicked
def check_play_button():
    global game_running, misses, hits, aliens
    mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()
    if button_x <= mouse_x <= button_x + button_width and button_y <= mouse_y <= button_y + button_height:
        if mouse_click[0]:  # Left click
            misses = 0
            hits = 0
            game_running = True
            aliens = []  # Reset aliens list
            spawn_aliens()

# Spawn aliens in a grid
def spawn_aliens():
    global aliens
    rows = 6  # Adjust to fit the screen vertically
    columns = 10  # Number of aliens horizontally
    spacing = 10  # Space between aliens
    for i in range(rows):
        for j in range(columns):
            alien_x = SCREEN_WIDTH - (j * (ALIEN_WIDTH + spacing) + ALIEN_WIDTH)  # Start from the right side
            alien_y = i * (ALIEN_HEIGHT + spacing)  # Stack vertically
            aliens.append(pygame.Rect(alien_x, alien_y, ALIEN_WIDTH, ALIEN_HEIGHT))

# Move aliens
def move_aliens():
    global aliens
    for alien in aliens:
        alien.x -= ALIEN_SPEED  # Move aliens horizontally left
        if alien.x + ALIEN_WIDTH <= 0:  # If alien goes off the left side, reset to the right
            alien.x = SCREEN_WIDTH
            alien.y += ALIEN_HEIGHT  # Move down one row

# Game over function
def game_over():
    font = pygame.font.Font(None, 48)
    game_over_text = font.render(f"Game Over! Hits: {hits}, Misses: {misses}", True, WHITE)
    screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 3))
    draw_play_button()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_running:  # Spacebar to shoot
                # Create a new bullet
                bullet_x = ship_x + SHIP_WIDTH  # Place bullet next to the ship
                bullet_y = ship_y + SHIP_HEIGHT // 2 - BULLET_HEIGHT // 2  # Center it vertically on the ship
                bullets.append(pygame.Rect(bullet_x, bullet_y, BULLET_WIDTH, BULLET_HEIGHT))
        elif event.type == pygame.MOUSEBUTTONDOWN:
            check_play_button()  # Check if Play button is clicked

    if not game_running:
        screen.fill(BLACK)
        game_over()
        pygame.display.flip()
        continue  # Skip the rest of the game logic if the game isn't running yet

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

    # Check for bullets that have passed the right side and count as a miss
    for bullet in bullets[:]:
        if bullet.x > SCREEN_WIDTH:
            misses += 1  # Count as a miss when the bullet goes off the screen
            bullets.remove(bullet)  # Remove the bullet

    # Remove bullets that are off-screen
    bullets = [bullet for bullet in bullets if bullet.x <= SCREEN_WIDTH]

    # Move aliens and check for bullet collisions
    move_aliens()

    for alien in aliens[:]:
        for bullet in bullets[:]:
            if alien.colliderect(bullet):
                bullets.remove(bullet)  # Remove the bullet
                aliens.remove(alien)  # Remove the alien
                hits += 1  # Increase the number of hits
                break  # Stop checking for more collisions after the first hit

    # Check if misses are greater than 3 (game over condition)
    if misses >= 3:
        game_running = False

    # Draw everything
    screen.fill(BLACK)  # Clear the screen
    screen.blit(ship_image, (ship_x, ship_y))  # Draw the ship
    for bullet in bullets:
        pygame.draw.rect(screen, BULLET_COLOR, bullet)  # Draw the bullets

    # Draw the aliens
    for alien in aliens:
        screen.blit(alien_image, alien.topleft)  # Draw the alien image

    # Display score
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Hits: {hits}  Misses: {misses}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)
