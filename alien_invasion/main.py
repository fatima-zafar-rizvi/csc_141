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
import pygame
from settings import Settings 
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from deadpool import Deadpool
from bullet import Bullet 
from enemy import Enemy




'''
# Set screen
screen = pygame.display.set_mode((1800, 860))

# Load background image
background = pygame.image.load('images/nyc.png').convert()

# Scale background image to fit the screen
background = pygame.transform.scale(background, (1800, 860))'''


class DeadpoolInvasion:
    '''Class to manage game assets and behavior'''

    def __init__(self):
        '''Initialize the game'''
        pygame.init()
        self.clock = pygame.time.Clock()

        self.settings = Settings()

        # Set screen
        self.screen = pygame.display.set_mode((1200, 800), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Deadpool Invasion")
        
        # Load and scale background image
        self.background = pygame.image.load('images/nyc.png').convert()
        self.background = pygame.transform.scale(self.background, 
            (self.settings.screen_width, self.settings.screen_height))
        
          
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        
        self.deadpool = Deadpool(self) 
        self.bullets = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self._create_fleet() 

        # Initialize the mixer for sound
        pygame.mixer.init()

        # Load the shooting sound
        self.shoot_sound = pygame.mixer.Sound('shoot.mp3')

        # Start Alien Invasion in an inactive state.
        self.game_active = False  

        # Make the Play button.
        self.play_button = Button(self, "Play")

        # Learderboard button
        self.leaderboard_button = Button(self, "Leaderboard")

        

    def run_game(self):
        '''Start the main loop for the game'''
        while True:
            self._check_events()

            if self.game_active:
                self.deadpool.update()
                self._update_bullets()
                self._update_enemies()
            
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        '''Respond to keypresses and mouse events'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                 self._check_keyup_events(event)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)


    def _check_keydown_events(self, event):
        '''Respond to keypresses'''
        if event.key == pygame.K_RIGHT:
            self.deadpool.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.deadpool.moving_left = True

        elif event.key == pygame.K_q:
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

    def _update_screen(self):
        '''Update images on the screen, and flip to the new screen'''
        #self.screen.fill(self.settings.bg_color)
        self.screen.blit(self.background, (0, 0))
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.deadpool.blitme()
        self.enemies.draw(self.screen)

        # Draw the score information.
        self.sb.show_score()

        # Draw the play button if the game is inactive.
        if not self.game_active:
            self.play_button.draw_button()

        pygame.display.flip()

    def _update_bullets(self):
        '''Update position of bullets and get rid of old bullets'''
        self.bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        
        self._check_bullet_enemy_collisions()

        # Check for any bullets that have hit enemies.
        # If so, get rid of the bullet and the enemy.
        collisions = pygame.sprite.groupcollide(
                self.bullets, self.enemies, True, True)
        
        if not self.enemies:
            # Destroy existing bullets and create new fleet.
            self.bullets.empty()
            self._create_fleet()

    def _update_enemies(self):
        """Check if the fleet is at an edge, then update positions."""
        self._check_fleet_edges()
        self.enemies.update()

        # Look for alien-ship collisions.
        if pygame.sprite.spritecollideany(self.deadpool, self.enemies):
            self._deadpool_hit()

        # Look for enemies hitting the bottom of the screen.
        self._check_enemies_bottom()

    def _check_bullet_enemy_collisions(self):
        '''Check for bullet-enemy collisions'''
        collisions = pygame.sprite.groupcollide(self.bullets, self.enemies,
                                                 True, True)
        
        if collisions:
            for enemies in collisions.values():
                self.stats.score += self.settings.enemy_points * len(enemies)
            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.enemies:
            # Destroy existing bullets and create new fleet
            self.bullets.empty()
            self._create_fleet()  
            self.settings.increase_speed()

            # Increase level.
            self.stats.level += 1
            self.sb.prep_level()

    def _create_fleet(self):
        '''Create fleet of enemies'''
        # Create an alien and keep adding aliens until there's no room left.
        # Spacing between aliens is one alien width.
        enemy = Enemy(self)
        enemy_width, enemy_height = enemy.rect.size

        current_x, current_y = enemy_width, enemy_height
        while current_y < (self.settings.screen_height - 3 * enemy_height):
            while current_x < (self.settings.screen_width - 2 * enemy_width):
                self._create_enemy(current_x, current_y)
                current_x += 2 * enemy_width

            # Finished a row; reset x value, and increment y value.
            current_x = enemy_width
            current_y += 2 * enemy_height

    def _create_enemy(self, x_position, y_position):
        '''Create an enemy and place it in the fleet'''
        new_enemy = Enemy(self)
        new_enemy.x = x_position
        new_enemy.rect.x = x_position
        new_enemy.rect.y = y_position
        self.enemies.add(new_enemy)



    def _check_play_button(self, mouse_pos):
        '''Start a new game when the player clicks Play'''
        ''' button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            # Reset the game settings.
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_deadpools()
            self.game_active = True

            # Get rid of any remaining bullets and aliens.
            self.bullets.empty()
            self.enemies.empty()

            # Create a new fleet and center the deadpool.
            self._create_fleet()
            self.deadpool.center_deadpool()

            # Hide the mouse cursor.
            pygame.mouse.set_visible(False)'''
        
        if self.play_button.rect.collidepoint(mouse_pos) and not self.game_active:
            # Start a new game
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_deadpools()
            self.game_active = True
            self.bullets.empty()
            self.enemies.empty()
            self._create_fleet()
            self.deadpool.center_deadpool()
            pygame.mouse.set_visible(False)
        elif self.leaderboard_button.rect.collidepoint(mouse_pos):
            # Show the leaderboard
            self._show_leaderboard()


    def _show_leaderboard(self):
        """Display the high scores."""
        self.screen.fill(self.settings.bg_color)
    
        # Display title
        font = pygame.font.SysFont(None, 48)
        title = font.render("Leaderboard", True, (255, 255, 255))
        title_rect = title.get_rect(center=(self.settings.screen_width // 2, 50))
        self.screen.blit(title, title_rect)

        # Display scores
        font = pygame.font.SysFont(None, 36)
        y_offset = 100
        for index, score in enumerate(self.stats.high_scores, 1):
            score_text = font.render(f"{index}. {score}", True, (255, 255, 255))
            score_rect = score_text.get_rect(center=(self.settings.screen_width // 2, y_offset))
            self.screen.blit(score_text, score_rect)
            y_offset += 40

        pygame.display.flip()

        # Wait for the user to exit the leaderboard
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    return



    def _check_fleet_edges(self):
        '''Respond appropriately if any enemies have reached an edge'''
        for enemy in self.enemies.sprites():
            if enemy.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        '''Drop the entire fleet and change the fleet's direction'''
        for enemy in self.enemies.sprites():
            enemy.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _deadpool_hit(self):
        """Respond to the deadpool being hit by enemy."""
        '''if self.stats.deadpools_left > 0:
        
            # Decrement deadpools_left, and update scoreboard.
            self.stats.deadpools_left -= 1
            self.sb.prep_deadpools()

            # Get rid of any remaining bullets and enemies.
            self.bullets.empty()
            self.enemies.empty()

            # Create a new fleet and center the deadpool.
            self._create_fleet()
            self.deadpool.center_deadpool()

            # Pause.
            sleep(0.5)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)'''
        
        if self.stats.deadpools_left > 0:
            self.stats.deadpools_left -= 1
            self.sb.prep_deadpools()
            self.bullets.empty()
            self.enemies.empty()
            self._create_fleet()
            self.deadpool.center_deadpool()
            sleep(0.5)
        else:
            self.stats.save_high_score(self.stats.score)  # Save score if it's high
            self.game_active = False
            pygame.mouse.set_visible(True)


    def _check_enemies_bottom(self):
        """Check if any enemies have reached the bottom of the screen."""
        for enemy in self.enemies.sprites():
            if enemy.rect.bottom >= self.settings.screen_height:
                # Treat this the same as if the deadpool got hit.
                self._deadpool_hit()
                break


        
if __name__ == '__main__':
    dp = DeadpoolInvasion()
    dp.run_game()