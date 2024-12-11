class GameStats:
    '''Track stats for Deadpool Invasion'''

    def __init__(self, dp_game):
        '''Initialize stats'''
        self.settings = dp_game.settings
        self.reset_stats()

    def reset_stats(self):
        '''Initialize stats that can change during the game'''
        # Start with the player having 3 Deadpool lives
        self.deadpool_left = self.settings.deadpool_limit
        # Initialize score and level
        self.score = 0
        self.level = 1

    def increment_score(self, points):
        '''Increment the score by given points'''
        self.score += points

    def level_up(self):
        '''Increase the level of the game'''
        self.level += 1

    def game_over(self):
        '''Check if the game is over'''
        return self.deadpool_left <= 0
