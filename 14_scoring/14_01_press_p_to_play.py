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
ALIEN_SPEED = 2
try:
    alien_image = pygame.image.load('images/alien.png')  # Load the alien image
    alien_image = pygame.transform.scale(alien_image, (ALIEN_WIDTH, ALIEN_HEIGHT))  # Scale to the desired size
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

# Alien list
aliens = []

# Counters
ship_hits = 0  # Track how many times the ship is hit
alien_hits = 0  # Track how many aliens are hit

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Game state (True for running, False for paused)
game_running = False

# Create a fleet of aliens
def create_aliens():
    for _ in range(5):  # Create 5 aliens
        alien_x = random.randint(SCREEN_WIDTH // 2, SCREEN_WIDTH - ALIEN_WIDTH)
        alien_y = random.randint(0, SCREEN_HEIGHT - ALIEN_HEIGHT)
        aliens.append(pygame.Rect(alien_x, alien_y, ALIEN_WIDTH, ALIEN_HEIGHT))

# Check if bullet hits alien
def check_collision():
    global aliens, bullets, alien_hits
    for bullet in bullets[:]:
        for alien in aliens[:]:
            if bullet.colliderect(alien):
                aliens.remove(alien)  # Remove the alien
                bullets.remove(bullet)  # Remove the bullet
                alien_hits += 1  # Increase the number of aliens hit
                break  # Exit the loop once a collision is detected

# Check if an alien hits the ship
def check_ship_collision():
    global ship_hits
    for alien in aliens:
        if alien.colliderect(pygame.Rect(ship_x, ship_y, SHIP_WIDTH, SHIP_HEIGHT)):
            ship_hits += 1  # Increase the number of times the ship is hit
            aliens.remove(alien)  # Remove the alien when it hits the ship
            break  # Stop after the first collision

# Start the game (called when player presses P)
def start_game():
    global game_running
    game_running = True
    create_aliens()  # Create the aliens when the game starts

# Display a start screen with instructions
def show_start_screen():
    font = pygame.font.Font(None, 36)
    start_text = font.render("Press 'P' to Start", True, WHITE)
    screen.fill(BLACK)
    screen.blit(start_text, (SCREEN_WIDTH // 2 - start_text.get_width() // 2, SCREEN_HEIGHT // 2))
    pygame.display.flip()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p and not game_running:  # Press P to start the game
                start_game()
            if event.key == pygame.K_SPACE and game_running:  # Spacebar to shoot
                # Create a new bullet
                bullet_x = ship_x + SHIP_WIDTH  # Place bullet next to the ship
                bullet_y = ship_y + SHIP_HEIGHT // 2 - BULLET_HEIGHT // 2  # Center it vertically on the ship
                bullets.append(pygame.Rect(bullet_x, bullet_y, BULLET_WIDTH, BULLET_HEIGHT))

    if not game_running:
        show_start_screen()
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

    # Remove bullets that are off-screen
    bullets = [bullet for bullet in bullets if bullet.x <= SCREEN_WIDTH]

    # Move aliens
    for alien in aliens:
        alien.x -= ALIEN_SPEED  # Move aliens toward the ship

    # Check for collisions between bullets and aliens
    check_collision()

    # Check if aliens hit the ship
    check_ship_collision()

    # Check if all aliens are off the screen (game over condition)
    if all(alien.x < 0 for alien in aliens):  # If all aliens are off the screen
        print(f"Game Over! You hit {alien_hits} aliens and the ship was hit {ship_hits} times.")
        break

    # Draw everything
    screen.fill(BLACK)  # Clear the screen
    screen.blit(ship_image, (ship_x, ship_y))  # Draw the ship
    for bullet in bullets:
        pygame.draw.rect(screen, BULLET_COLOR, bullet)  # Draw the bullets
    for alien in aliens:
        screen.blit(alien_image, (alien.x, alien.y))  # Draw the aliens using the alien image

    # Display scores (hit counts)
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Aliens Hit: {alien_hits}   Ship Hits: {ship_hits}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)