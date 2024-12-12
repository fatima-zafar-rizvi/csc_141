import pygame.font

class Button:
    '''A class to build buttons for the game'''

    def __init__(self, dp_game, msg):
        '''Initialize button attributes'''
        self.screen = dp_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set the dimensions and properties of the button
        self.width, self.height = 200, 50
        self.button_color = (255, 0, 0)
        self.hover_color = (139, 0, 0)
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 48)

        # Build the button's rect object and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # The button message needs to be prepped only once
        self._prep_msg(msg)



    def _prep_msg(self, msg):
        '''Turn message into rendered image and center text on the button'''
        self.msg_image = self.font.render(msg, True, 
                                          self.text_color, 
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Draw hover button and then draw message."""
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(self.screen, self.hover_color, self.rect)
        else:
            pygame.draw.rect(self.screen, self.button_color, self.rect)
        
        # Draw the text
        self.screen.blit(self.msg_image, self.msg_image_rect)