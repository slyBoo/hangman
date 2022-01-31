from ntpath import join
import random


#local functions
def select_word():
    with open("words2.txt", 'r') as f:
        words = f.read().strip().split()
        return random.choice(words)


def find_all(word, char):
    return [pos for pos, c in enumerate(word) if c == char.upper()]


class Hangman():
    def __init__(self):
        self.word = select_word().upper()
        self.g_word = ["-"] * len(self.word)
        self.lives = 5
        self.won = False
        print(f"Word selected is {''.join(self.g_word):s}, the length of the word is {len(self.word):d} and you have {self.lives:d} guesses!")

    
    def reduce_life(self):
        self.lives = self.lives - 1
     
    #Getters
    def get_word(self):
        return self.word


    def get_lives(self):
        return self.lives


    def get_won(self):
        return self.won


    def change_g_word(self, char):
        positions = find_all(self.word, char)
        for pos in positions:
            self.g_word[pos] = char
        return self.g_word


    def win_con(self):
        return self.word == "".join(self.g_word)