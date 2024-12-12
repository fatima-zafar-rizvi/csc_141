import pygame.font
from pygame.sprite import Group
from deadpool import Deadpool

class Scoreboard:
    """A class to report scoring information."""
    def __init__(self, dp_game):
        """Initialize scorekeeping attributes."""
        self.dp_game = dp_game
        self.screen = dp_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = dp_game.settings
        self.stats = dp_game.stats
        
        # Font settings for scoring information.
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare the initial score images.
        self.prep_score()
        self.prep_level()
        self.prep_deadpools()

    def prep_score(self):
        """Turn the score into a rendered image."""
        rounded_score = round(self.stats.score, -1)
        score_str = f"{rounded_score:,}"
        self.score_image = self.font.render(score_str, True,
            self.text_color, self.settings.bg_color)
        
        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Draw scores, level, and ships to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.deadpools.draw(self.screen)

    def prep_level(self):
        """Turn the level into a rendered image."""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True,
            self.text_color, self.settings.bg_color)
        
        # Position the level below the score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_deadpools(self):
        """Show how many deadpools are left."""
        self.deadpools = Group()
        for deadpool_number in range(self.stats.deadpools_left):
            deadpool = Deadpool(self.dp_game)
            deadpool.rect.x = 10 + deadpool_number * deadpool.rect.width
            deadpool.rect.y = 10
            self.deadpools.add(deadpool)
