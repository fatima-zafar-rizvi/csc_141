import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''A class to manage bullets fired from Deadpool.'''

    def __init__(self, dp_game):
        super().__init__()
        self.screen = dp_game.screen
        self.settings = dp_game.settings
        self.color = self.settings.bullet_color
        self.image = pygame.image.load('images/bullet.png')
        self.image = self.image.convert()
        self.image = pygame.transform.scale(self.image, (self.settings.bullet_width, self.settings.bullet_height))
        
        # Set the transparent color (if needed)
        self.image.set_colorkey((0, 0, 0))  

        # Create a bullet rect
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = dp_game.deadpool.rect.midtop

        # Store bullet's position as a float
        self.y = float(self.rect.y)

    def update(self):
        '''Move bullet up the screen and check if it's off-screen'''
        # Update exact position of the bullet
        self.y -= self.settings.bullet_speed
        # Update the rect position
        self.rect.y = self.y

        # If the bullet is off the screen, remove it
        if self.rect.bottom <= 0:
            self.kill()  # Remove the sprite from the group
        else:
            self.draw_bullet()

    def draw_bullet(self):
        '''Draw the bullet onto the screen'''
        self.screen.blit(self.image, self.rect)
