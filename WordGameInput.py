import random

class WordGame:

    # Requests how the word performs in the Word Game from user where:
    # g in the results coresponds with correct letters
    # y in the results coresponds with letters in the word at the wrong place
    # e in rhe results coresponds with a letter not in the word
    def try_val(self, guess):
        correctness = input("Input result with format of r isn't in word, y is at wrong place, g is at the right place> ")

        return correctness
