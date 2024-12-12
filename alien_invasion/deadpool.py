import pygame
from pygame.sprite import Sprite
# from settings import Settings

class Deadpool(Sprite):
    '''A class to manage Deadpool'''

    def __init__(self, dp_game):
        """Initialize the ship and set its starting position."""
        super().__init__()
        self.screen = dp_game.screen
        self.settings = dp_game.settings
        # self.settings = dp_game.settings
        self.screen_rect = dp_game.screen.get_rect()

        # Load Deadpool image and get its rect
        self.image = pygame.image.load('images/deadpool.png')
        ''''''
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.image = self.image.convert()
        self.image.set_colorkey(self.image.get_at((1, 1)))
        ''''''
        self.rect = self.image.get_rect()

        # Start each Deadpool at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a float for the ship's exact horizontal position
        self.x = float(self.rect.x)

        # Movement flags; start with Deadpool not moving
        self.moving_right = False
        self.moving_left = False

    def update(self):
        '''Update Deadpool's position based on the movement flags'''
        # Move right if the flag is set and within the screen's right boundary
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.deadpool_speed

        # Move left if the flag is set and within the screen's left boundary
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.deadpool_speed

        # Update rect object from self.x
        self.rect.x = self.x

    def blitme(self):
        '''Draw Deadpool at his current location'''
        self.screen.blit(self.image, self.rect)

    def center_deadpool(self):
        '''Center Deadpool on the screen'''
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
