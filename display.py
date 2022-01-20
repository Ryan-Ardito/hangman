import os
from typing import List

from game import GameSession


def game_screen(game: GameSession) -> None:
    """Show a visual representation of the game state"""
    clear_screen()
    show_score(game.user.username, game.user.wins, game.user.losses)
    draw_man(len(game.misses))
    show_wrong_guesses(game.misses)
    if game.lost():
        game_over(game.secret_word, win=False)
    elif game.won():
        game_over(game.secret_word, win=True, perfect=(not game.misses))
    else:
        show_hits(game.hidden_word)


def show_score(username: str, wins: int, losses: int) -> None:
    # Draw the top of the gallows; show username and wins/losses
    print(f' ____  {username}')
    print(f' |/ |  W:{wins} L:{losses}')


def draw_man(misses: int) -> None:
    # Draw the hanging man based on the number of misses.
    if misses < 1:
        print(' |')
    else:
        print(' |  0')
    if misses < 2:
        print(' |')
    elif misses < 5:
        print(' |  |')
    elif misses < 6:
        print(' | /|')
    else:
        print(r' | /|\ ')
    if misses < 3:
        print(' |')
    elif misses < 4:
        print(' | /')
    else:
        print(r' | / \ ')
    print('_|____')


def show_wrong_guesses(misses: list) -> None:
    print(f"Misses: {' '.join(misses)}")


def show_hits(hidden_word: list) -> None:
    print(''.join(hidden_word))


def get_input() -> str:
    """Accept user input and return in a string"""
    user_input = input('Guesses: ')
    return user_input.lower()


def game_over(secret_word: str, win: bool, perfect: bool = False) -> None:
    print(secret_word)
    if perfect:
        print('Perfect!', end=' ')
    elif win:
        print('You win!', end=' ')
    else:
        print('You lose.', end=' ')


def play_again() -> bool:
    if input('Play again? Y/n: ') in ('', 'y', 'Y', 'yes', 'Yes', 'YES'):
        return True
    else:
        return False


def clear_screen() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')


def help_screen(commands: List[str]) -> None:
    clear_screen()
    print(f'Commands: {", ".join(commands)}\n')
    input('Press enter to continue')


def login_screen() -> str:
    clear_screen()
    return input('username: ')


def about_screen() -> None:
    clear_screen()
    print('In hangman, the computer randomly selects a word for you to guess.')
    print('Enter as many letters as you like and they will be evaluated.')
    print('Six incorrect letters and mr. stick figure is hanged.\n')
    print('Hangman supports saving user score, wins/losses and wordlists')
    print('In the game, type help to see a list of commands.\n')
    input('Press enter to continue')


def wordlists_screen(all_lists, user_lists) -> list:
    clear_screen()
    new_lists = []
    # Show all lists
    for i, wordlist in enumerate(all_lists):
        selected = ' '
        if wordlist in user_lists:
            selected = '*'
        print(f'{i}. {selected} {wordlist}')
    # Parse input
    user_input = input('Select wordlists by number: ')
    for char in set(user_input):
        if not char.isdigit() or int(char) > len(all_lists):
            continue
        new_lists.append(all_lists[int(char)])
    return new_lists
