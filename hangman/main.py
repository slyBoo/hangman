#!/usr/bin/env python3
import game

def guess_check(c, w):
    return c in w

def check_input(s):
    return len(s) == 1 and s.isalpha()

def main():
    yes_values = {"yes", "ye", "y"}
    keep_playing = True
    while keep_playing:
        new_game = game.Hangman()
        while new_game.get_lives() > 0 and not new_game.win_con():
            guess = input("Guess a letter: ").strip().upper()
            if guess == new_game.get_word():
                break

            while not check_input(guess):
                guess = input("Character must be a single character and a letter: ").strip().upper()

            if guess_check(guess, new_game.get_word()):
                guessed_word = new_game.change_g_word(guess)
                print("".join(guessed_word))
            else:
                new_game.reduce_life()
                print(f'Gusses remaining: {new_game.get_lives()}')

            

        if new_game.get_lives() > 0:
            print("You guessed it correctly!")
        else:
            print(f"You guessed it incorrectly!\nThe word was {new_game.get_word():s}")

        play = input("Keep playing? (y/n): ").lower()
        if play not in yes_values:
            keep_playing = False


if __name__ == "__main__":
    main()
