import json
from words import Words

users_file = 'users.json'


def get_all_users() -> dict:
    # Load user data
    try:
        with open(users_file, 'r') as file:
            all_users = json.load(file)
    except FileNotFoundError:
        all_users = {}
        with open(users_file, 'w') as file:
            json.dump(all_users, file)
    return all_users


class UserSession:
    """Handle user data"""
    default_user_data = {
        'wins': 0,
        'losses': 0,
        'wordlists': ['The_Oxford_3000.txt'],
        'saved_game': {} # {'secret_word': '', 'guesses': []}
    }

    def __init__(self, username):
        self.username: str = username
        self.all_users: dict = get_all_users()
        if self.username not in self.all_users:
            self.all_users[self.username] = self.default_user_data
        self.user_data: dict = self.all_users[self.username]
        self.words: Words = Words(self.wordlists)

    def save(self) -> None:
        """Save user data to JSON file"""
        # Guest is not persistent
        if self.username == 'guest':
            return
        with open('users.json', 'w') as file:
            json.dump(self.all_users, file, indent=4)

    @property
    def wins(self) -> int:
        return self.user_data['wins']

    @wins.setter
    def wins(self, val: int):
        self.user_data['wins'] = val

    @property
    def losses(self) -> int:
        return self.user_data['losses']

    @losses.setter
    def losses(self, val: int):
        self.user_data['losses'] = val

    @property
    def wordlists(self) -> list:
        return self.user_data['wordlists']

    @wordlists.setter
    def wordlists(self, val: list):
        self.user_data['wordlists'] = val
        self.save()
        # Instantiate new words object when wordlists change
        self.words = Words(self.wordlists)

    @property
    def saved_game(self) -> dict:
        return self.user_data['saved_game']

    @saved_game.setter
    def saved_game(self, val: dict):
        self.user_data['saved_game'] = val
        self.save()

