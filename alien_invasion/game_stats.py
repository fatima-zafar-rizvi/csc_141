class GameStats:
    '''Track stats for Deadpool Invasion'''

    def __init__(self, dp_game):
        """Initialize statistics."""
        self.settings = dp_game.settings
        self.reset_stats()
        self.game_active = False

        # Store a list of high scores for the leaderboard
        self.high_scores = [0] * 5  # Top 5 high scores initialized to 0

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.deadpools_left = self.settings.deadpool_limit
        self.score = 0
        self.level = 1

    def _load_high_scores(self):
        """Load high scores from a file."""
        try:
            with open("high_scores.txt", "r") as file:
                return [int(line.strip()) for line in file.readlines()]
        except FileNotFoundError:
            return [0] * 5  # Default leaderboard

    def save_high_score(self, new_score):
        """Save a new high score."""
        self.high_scores.append(new_score)
        self.high_scores = sorted(self.high_scores, reverse=True)[:5]
        with open("high_scores.txt", "w") as file:
            for score in self.high_scores:
                file.write(f"{score}\n")
