#!/usr/bin/env python3

from game import GameSession
import display
import command


def hangman():
    game = GameSession()

    # Program loop
    while True:

        # Game loop
        while not game.won() and not game.lost():
            display.game_screen(game)
            user_input = display.get_input()

            if command.execute(user_input, game):
                continue
            game.parse_guess(user_input)

        # Game over
        game.game_over()

        display.game_screen(game)

        if not display.play_again():
            command.quit(game)
        game.new_game()


if __name__ == '__main__':
    hangman()
