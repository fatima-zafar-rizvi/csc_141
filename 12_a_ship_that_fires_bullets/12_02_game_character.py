import sys
import pygame

class Deadpool:
    """A game class to display a character on a black background."""

    def __init__(self):
        """Initialize the game and resources."""
        pygame.init()

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0) 

        # Set up the screen
        self.screen = pygame.display.set_mode((self.screen_width, 
                                               self.screen_height))
        pygame.display.set_caption("Deadpool")

        # Load the character image
        self.character = pygame.image.load('images/deadpool.bmp')  

        # Set the charcter to a smaller size
        self.character = pygame.transform.scale(self.character, (150, 150))

        # Set the background color of the image to match the screen color 
        self.character.set_colorkey((0, 0, 0))  

        # Get the image's rect to position it at the center
        self.character_rect = self.character.get_rect()
        self.character_rect.center = (self.screen_width // 2, 
                                      self.screen_height // 2)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for events like quitting
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Fill the screen with the background color
            self.screen.fill(self.bg_color)

            # Draw the character image
            self.screen.blit(self.character, self.character_rect)

            # Update the display
            pygame.display.flip()


# Create an instance of the game and run it
if __name__ == "__main__":
    game = Deadpool()
    game.run_game()