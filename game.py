from player import UserSession


class GameSession:
    """Handle game data"""
    def __init__(self, username='guest'):
        # Instantiate guest user
        self.set_user(username)

    def set_user(self, username: str) -> None:
        if not username:
            return
        self.user = UserSession(username)
        self.new_game()

    def new_game(self) -> None:
        self.game_data = self.user.saved_game
        if not self.game_data:
            secret_word = self.user.words.random_word()
            self.game_data = {
                'secret_word'   : secret_word,
                'guesses'       : []
            }

    @property
    def secret_word(self) -> str:
        return self.game_data['secret_word']

    @property
    def guesses(self) -> list:
        return self.game_data['guesses']

    @property
    def hidden_word(self) -> list:
        return [c if c in self.guesses else '_' for c in self.secret_word]

    @property
    def misses(self) -> list:
        return [c for c in self.guesses if c not in self.secret_word]

    def game_over(self) -> None:
        """Trigger game over event"""
        if self.lost():
            self.user.losses += 1
        elif self.won():
            self.user.wins += 1
        self.save()

    def parse_guess(self, user_input: str) -> None:
        user_input = user_input.lower()
        for char in user_input:
            if not char.isalpha() or char in self.guesses:
                continue
            self.guesses.append(char)

    def save(self) -> None:
        # Don't save game state if game over or no guesses have been made
        if self.won() or self.lost() or not self.guesses:
            self.user.saved_game = {}
        # Save game state to user
        else:
            self.user.saved_game = self.game_data

    def won(self) -> bool:
        return ('_' not in self.hidden_word and len(self.misses) < 6)

    def lost(self) -> bool:
        return (len(self.misses) >= 6)

