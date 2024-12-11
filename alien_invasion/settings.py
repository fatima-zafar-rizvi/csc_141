class Settings:
    '''A class to start all settings for Deadpool Invasion'''

    def __init__(self):
        '''Initialize game settings'''
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Deadpool's speed
        self.deadpool_speed = 4.5
        self.deadpool_limit = 3  # Max lives for Deadpool

        # Bullet settings
        self.bullet_speed = 7.0  # Adjusted bullet speed for smoother gameplay
        self.bullet_width = 5    # Slightly larger bullet width
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 20  # Reasonable number of bullets

        # Enemy settings
        self.fleet_speed = 6.0
        self.fleet_drop_speed = 10
        # Fleet direction of 1 represents right, -1 represents left
        self.fleet_direction = 1

        # Game speed
        self.speedup_scale = 1.1

        # Initialize dynamic settings
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        '''Initialize settings that change throughout the game'''
        self.deadpool_speed = 4.5
        self.bullet_speed = 7.0  # Adjusted bullet speed
        self.fleet_speed = 6.0

        # Fleet direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

    def increase_speed(self):
        '''Increase speed settings'''
        self.deadpool_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.fleet_speed *= self.speedup_scale
