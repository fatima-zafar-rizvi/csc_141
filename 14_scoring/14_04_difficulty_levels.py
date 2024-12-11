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

# Game settings class
class Settings:
    def __init__(self):
        self.alien_speed = 1  # Initial alien speed
        self.bullet_speed = 7  # Bullet speed
        self.fleet_drop_speed = 10  # Speed at which aliens drop
        self.fleet_direction = 1  # 1 means moving right, -1 means left
        self.alien_points = 50  # Points for each alien
        self.ship_speed = 5  # Speed of the ship
        self.difficulty = "Medium"  # Default difficulty

    def set_difficulty(self, difficulty):
        if difficulty == "Easy":
            self.alien_speed = 0.5
            self.bullet_speed = 5
            self.fleet_drop_speed = 5
            self.alien_points = 30
            self.ship_speed = 6
        elif difficulty == "Medium":
            self.alien_speed = 1
            self.bullet_speed = 7
            self.fleet_drop_speed = 10
            self.alien_points = 50
            self.ship_speed = 5
        elif difficulty == "Hard":
            self.alien_speed = 1.5
            self.bullet_speed = 8
            self.fleet_drop_speed = 15
            self.alien_points = 100
            self.ship_speed = 4

# Initialize Settings
settings = Settings()

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Alien Invasion")

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

# Alien settings
ALIEN_WIDTH = 50
ALIEN_HEIGHT = 50
ALIEN_COLOR = (0, 255, 0)

# Initialize ship position
ship_x = (SCREEN_WIDTH - SHIP_WIDTH) // 2
ship_y = SCREEN_HEIGHT - SHIP_HEIGHT - 10

# Create difficulty buttons
button_width = 200
button_height = 50
button_x = SCREEN_WIDTH // 2 - button_width // 2
button_y = SCREEN_HEIGHT // 2 - button_height // 2

# Create a button for each difficulty level
def draw_difficulty_buttons():
    font = pygame.font.Font(None, 36)
    
    # Easy button
    easy_text = font.render("Easy", True, WHITE)
    pygame.draw.rect(screen, (0, 255, 0), (button_x, button_y, button_width, button_height))
    screen.blit(easy_text, (button_x + button_width // 2 - easy_text.get_width() // 2,
                           button_y + button_height // 2 - easy_text.get_height() // 2))
    
    # Medium button
    medium_text = font.render("Medium", True, WHITE)
    pygame.draw.rect(screen, (0, 0, 255), (button_x, button_y + 60, button_width, button_height))
    screen.blit(medium_text, (button_x + button_width // 2 - medium_text.get_width() // 2,
                              button_y + 60 + button_height // 2 - medium_text.get_height() // 2))
    
    # Hard button
    hard_text = font.render("Hard", True, WHITE)
    pygame.draw.rect(screen, (255, 0, 0), (button_x, button_y + 120, button_width, button_height))
    screen.blit(hard_text, (button_x + button_width // 2 - hard_text.get_width() // 2,
                            button_y + 120 + button_height // 2 - hard_text.get_height() // 2))

# Check if a button was clicked
def check_difficulty_button_click():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()
    
    if button_x <= mouse_x <= button_x + button_width:
        if button_y <= mouse_y <= button_y + button_height and mouse_click[0]:
            settings.set_difficulty("Easy")
            return True
        elif button_y + 60 <= mouse_y <= button_y + 60 + button_height and mouse_click[0]:
            settings.set_difficulty("Medium")
            return True
        elif button_y + 120 <= mouse_y <= button_y + 120 + button_height and mouse_click[0]:
            settings.set_difficulty("Hard")
            return True
    return False

# Game state
game_running = False

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not game_running:
                if check_difficulty_button_click():  # Check if difficulty button was clicked
                    game_running = True

    if not game_running:
        screen.fill(BLACK)
        draw_difficulty_buttons()
        pygame.display.flip()
        continue  # Skip the rest of the game logic if the game isn't running yet

    # Get keys pressed
    keys = pygame.key.get_pressed()

    # Game logic (e.g., moving ship, shooting bullets, etc.)
    # TODO: Add logic for moving the ship, shooting bullets, and handling aliens

    # Draw everything
    screen.fill(BLACK)
    screen.blit(ship_image, (ship_x, ship_y))  # Draw the ship

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)
