import sys

import display
import words
from game import GameSession


def execute(user_input: str, game: GameSession) -> bool:
    """Check user input for commands and execute."""
    if user_input not in command_map:
        return False
    command_map[user_input](game)
    return True


def about(*_unused) -> None:
    display.about_screen()


def help_screen(*_unused) -> None:
    display.help_screen(list(command_map.keys()))


def quit(game: GameSession) -> None:
    game.save()
    display.clear_screen()
    sys.exit()


def user_login(game: GameSession) -> None:
    username = display.login_screen()
    if not username:
        return
    game.set_user(username)


def select_wordlists(game: GameSession) -> None:
    all_lists = words.all_words_files()
    user_lists = game.user.wordlists
    new_lists = display.wordlists_screen(all_lists, user_lists)
    if not new_lists:
        return
    game.user.wordlists = new_lists
    # Start a new game if the secret word could be from a unselected list
    if not set(user_lists).issubset(set(new_lists)):
        game.new_game()


command_map = {
    'about': about,
    'help': help_screen,
    'quit': quit,
    'login': user_login,
    'wordlists': select_wordlists
}
