#!/usr/bin/env python3


def check_len(s, n):
    if len(s) >= n:
        return True
    else:
        return False


def main(file):
    with open(file, 'r') as f:
        lines = f.read().strip().split()
    with open( "words2.txt", 'w') as f2:
        for line in lines:
            word = line.split()[0]
            if word.isalpha() and check_len(word, 5):
                f2.write(word + "\n")


if __name__ == "__main__":
    main(".\FileChanger\words.txt")