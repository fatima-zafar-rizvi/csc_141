class GameStats:
    '''Track stats for Deadpool Invasion'''

    def __init__(self, dp_game):
        """Initialize statistics."""
        self.settings = dp_game.settings
        self.reset_stats()
        self.game_active = False

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.deadpools_left = self.settings.deadpool_limit
        self.score = 0
        self.level = 1

    # No need for the high scores list or saving/loading of scores anymore
    # Remove the save_high_score method or leave it without leaderboard functionality
