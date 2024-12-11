import pygame
from pygame.sprite import Sprite 
from settings import Settings

class Enemy(Sprite):
    '''A class to represent a single enemy in the fleet'''

    def __init__(self, dp_game):
        '''Initialize the enemy and set its starting position'''
        super().__init__()
        self.screen = dp_game.screen
        self.settings = dp_game.settings
        self.screen_rect = dp_game.screen.get_rect()

        # Load the enemy image and set its rect attribute
        self.image = pygame.image.load('images/deadpool.bmp')
        self.image = pygame.transform.scale(self.image, (180, 170))
        self.rect = self.image.get_rect()

        # Start each new enemy near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height  # You can set this to a different y-value if necessary
        
        # Ensure enemy starts from top of the screen
        # This can be adjusted if needed for more specific placement
        self.rect.top = self.screen_rect.top  

        # Store the enemy's exact horizontal position as a float
        self.x = float(self.rect.x)
    
    def check_edges(self):
        '''Return True if enemy is at the edge of the screen'''
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)
    
    def update(self):
        '''Move enemy to the right'''
        self.x += self.settings.fleet_speed * self.settings.fleet_direction
        self.rect.x = self.x