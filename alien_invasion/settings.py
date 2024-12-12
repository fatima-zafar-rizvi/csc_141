class Settings:
    '''A class to start all settings for Deadpool Invasion'''

    def __init__(self):
        '''Initialize game settings'''
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)

        # Deadpool's settings
        self.deadpool_speed = 5.0
        self.deadpool_limit = 3  # Max lives for Deadpool

        # Bullet settings
        self.bullet_speed = 10.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 255, 0)
        self.bullets_allowed = 100


        # Enemy settings
        self.enemy_speed = 5.0
        self.fleet_drop_speed = 10
        # Fleet direction of 1 represents right, -1 represents left
        self.fleet_direction = 1

        # How quickly the game speeds up
        self.speedup_scale = 1.1
 
        # How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        # Initialize settings that change throughout the game
        self.deadpool_speed = 5.0
        self.bullet_speed = 10.0  # Adjusted bullet speed
        self.enemy_speed = 5.0

        # Fleet direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Scoring settings
        self.enemy_points = 50

    def increase_speed(self):
        # Increase speed settings
        self.deadpool_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.enemy_speed *= self.speedup_scale

        self.enemy_points = int(self.enemy_points * self.score_scale)
        print(self.enemy_points)
