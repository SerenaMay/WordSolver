import random

class WordGame:
    # Creates WordGame object either from provided list or a provided word
    def __init__(self, base_word=""):
        if base_word == "":
            words = open("words.txt", "rt")
            self.word = random.choice(words.read().splitlines())
        else:
            self.word = base_word.lower()

    # Tries a guess value against the base word, giving a response where:
    # g in the results coresponds with correct letters
    # y in the results coresponds with letters in the word at the wrong place
    # e in rhe results coresponds with a letter not in the word
    def try_val(self, guess):
        correctness = ""
        for x in range(0, 5):
            if guess[x] == self.word[x]:
                correctness += "g"
            elif guess[x] in self.word:
                correctness += "y"
            else:
                correctness += "r"
        return correctness
