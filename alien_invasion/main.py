'''
Take control of Deadpool at the bottom of the screen and embark on an 
action-packed adventure! You can expertly maneuver left and right while 
unleashing a barrage of bullets at the ruthless enemies descending upon you. 
These foes will move across and down the screen, and your mission is to shoot 
them down one by one. Once you obliterate a group of enemies, get 
ready—faster, more challenging foes will emerge! Remember, if an enemy reaches 
Deadpool, you'll have three lives to survive before the game is over. 
Get ready to prove your skills and have a blast!
'''

import sys 
from time import sleep
import pygame  # type: ignore
from settings import Settings 
from game_stats import GameStats
from button import Button
from deadpool import Deadpool
from bullet import Bullet 
from enemy import Enemy

# Initialize pygame
pygame.init()


# Set screen
screen = pygame.display.set_mode((1800, 860))

# Load background image
background = pygame.image.load('images/nyc.png')

# Scale background image to fit the screen
background = pygame.transform.scale(background, (1800, 860))


class DeadpoolInvasion:
    '''Class to manage game assets and behavior'''

    def __init__(self):
        '''Initialize the game'''
        self.clock = pygame.time.Clock()   
        self.settings = Settings()

        # Initialize the mixer for sound
        pygame.mixer.init()

        # Load the shooting sound
        self.shoot_sound = pygame.mixer.Sound('shoot.mp3')

        # Run the game full screen
        self.screen = pygame.display.set_mode((1800, 800), pygame.FULLSCREEN)
        pygame.display.set_caption("Deadpool Invasion")

        # Create an instance to store game stats
        self.stats = GameStats(self)
        self.deadpool = Deadpool(self)
        self.bullets = pygame.sprite.Group()
        self.fleet = pygame.sprite.Group()  # Renamed 'enemy' to 'fleet'
        self._create_fleet()  # This will be fixed in the following way

        self.game_active = False  # Corrected this initialization
        self.play_button = Button(self, "Play!")

    def run_game(self):
        '''Start the main loop for the game'''
        while True:
            screen.blit(background, (0, 0))

            if self.game_active:
                self.deadpool.update()
                self._update_bullets()  
                self._update_fleets()  # Corrected this line (it should be _update_fleets)
            
            self._update_screen()
            self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)
                elif event.type == pygame.K_ESCAPE:
                    sys.exit()

            pygame.display.flip()

    def _check_bullet_enemy_collisions(self):
        '''Check for bullet-enemy collisions'''
        collisions = pygame.sprite.groupcollide(self.bullets, self.fleet, 
                                                True, True)

        if not self.fleet:  # Check if the fleet is empty
            # Destroy existing bullets and create new fleet
            self.bullets.empty()
            self._create_fleet()  # Fixed by adding parentheses
            self.settings.increase_speed()

    def _update_bullets(self):
        '''Update position of bullets and get rid of old bullets'''
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_enemy_collisions()

    def _update_screen(self):
        '''Update images on the screen, and flip to the new screen'''
        self.screen.fill(self.settings.bg_color)
        self.deadpool.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.fleet.draw(self.screen)
        pygame.display.flip()

    def _check_events(self):
        '''Respond to keypresses and mouse events'''
        for event in pygame.event.get():
            if event.type == pygame.K_ESCAPE:
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_play_button(self, mouse_pos):
        '''Start a new game when the player clicks Play'''
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.game_active = True

            self.bullets.empty()
            self.fleet.empty()

            self._create_fleet()
            self.deadpool.center_deadpool()

            pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event):
        '''Respond to keypresses'''
        if event.key == pygame.K_RIGHT:
            self.deadpool.moving_right = True
            self.deadpool.facing_left = False
        elif event.key == pygame.K_LEFT:
            self.deadpool.moving_left = True
            self.deadpool.facing_left = True
        elif event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        '''Respond to key releases'''
        if event.key == pygame.K_RIGHT:
            self.deadpool.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.deadpool.moving_left = False

    def _fire_bullet(self):
        '''Create a new bullet and add it to the bullets group'''
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

            # Play the shooting sound when a bullet is fired
            self.shoot_sound.play()

    def _create_fleet(self):
        '''Create fleet of enemies'''
        for row_num in range(3):
            for enemy_num in range(5):
                self._create_enemy(enemy_num, row_num)

    def _create_fleet_row(self, x_position, y_position):
        '''Create an enemy and place it in the row'''
        new_enemy = Enemy(self)
        new_enemy.x = x_position
        new_enemy.rect.x = x_position
        new_enemy.rect.y = y_position
        self.fleet.add(new_enemy)

    def _create_fleet(self, x_position, y_position):
        '''Create an enemy and place it in the row'''
        new_enemy = Enemy(self)
        new_enemy.x = x_position
        new_enemy.rect.x = x_position
        new_enemy.rect.y = y_position
        self.fleet.add(new_enemy)

    def _check_fleet_edges(self):
        '''Respond appropriately if any enemies have reached an edge'''
        for enemy in self.fleet.sprites():
            if enemy.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        '''Drop the entire fleet and change the fleet's direction'''
        for enemy in self.fleet.sprites():
            enemy.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_fleets(self):
        '''Update the positions of all the enemies in the fleet'''
        self._check_fleet_edges()
        self.fleet.update()

        if pygame.sprite.spritecollideany(self.deadpool, self.fleet):
            self._ship_hit()

        self._check_fleet_bottom()

    def _ship_hit(self):
        '''Respond to the deadpool being hit by an enemy'''
        if self.stats.deadpool_left > 0:
            self.stats.deadpool_left -= 1
            self.bullets.empty()
            self.fleet.empty()

            self._create_fleet()
            self.deadpool.center_deadpool()

            sleep(0.5)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)

    def _check_fleet_bottom(self):
        '''Check if any enemies have reached the bottom of the screen'''
        for enemy in self.fleet.sprites():
            if enemy.rect.bottom >= self.settings.screen_height:
                self._ship_hit()
                break

if __name__ == '__main__':
    dp = DeadpoolInvasion()
    dp.run_game()
