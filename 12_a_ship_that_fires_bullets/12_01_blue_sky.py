import sys
import pygame

class BlueSky:
    # Overall class to mangae game assets and behaviour.

    def __init__(self):
        # Initialize game and create game resources.
        pygame.init()

        # Set up the screen.
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Blue Sky")

        # Set the background color
        self.bg_color = (0, 0, 255)
        
    def run_game(self):
        # Start main loop for the game.
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Redraw the screen during each pass through the loop.
            self.screen.fill(self.bg_color)

            # Make the most recently draw screen visible.
            pygame.display.flip()

# Create an instance of the game and run it.
if __name__ == "__main__":
    game = BlueSky()
    game.run_game()
