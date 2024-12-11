import pygame
import sys

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

# Target settings
TARGET_WIDTH = 40
TARGET_HEIGHT = 40
TARGET_SPEED = 2
target_x = SCREEN_WIDTH - TARGET_WIDTH

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Target Practice")

# Ship starting position
ship_x = 50
ship_y = (SCREEN_HEIGHT - SHIP_HEIGHT) // 2

# Bullet list
bullets = []

# Target position and movement
target_y = SCREEN_HEIGHT // 2
target_direction = 1  # 1 for moving down, -1 for moving up

# Counters
misses = 0
hits = 0

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Game state
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
    global game_running, misses, hits
    mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()
    if button_x <= mouse_x <= button_x + button_width and button_y <= mouse_y <= button_y + button_height:
        if mouse_click[0]:  # Left click
            misses = 0
            hits = 0
            game_running = True

# Game over function
def game_over():
    font = pygame.font.Font(None, 48)
    game_over_text = font.render(f"Game Over! Hits: {hits}, Misses: {misses}", True, WHITE)
    screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 3))
    draw_play_button()

# Start the game (called when player presses P)
def start_game():
    global game_running, target_y, target_direction, misses, hits
    game_running = True
    target_y = SCREEN_HEIGHT // 2
    target_direction = 1
    misses = 0
    hits = 0
    bullets.clear()  # Clear any bullets from previous game

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

    # Move target up and down
    target_y += TARGET_SPEED * target_direction
    if target_y <= 0 or target_y >= SCREEN_HEIGHT - TARGET_HEIGHT:
        target_direction *= -1  # Reverse direction when it hits the screen edge

    # Check for collisions between bullets and target
    for bullet in bullets[:]:
        if pygame.Rect(target_x, target_y, TARGET_WIDTH, TARGET_HEIGHT).colliderect(bullet):
            bullets.remove(bullet)  # Remove the bullet
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
    pygame.draw.rect(screen, RED, (SCREEN_WIDTH - TARGET_WIDTH, target_y, TARGET_WIDTH, TARGET_HEIGHT))  # Draw the target

    # Display score
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Hits: {hits}  Misses: {misses}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)
