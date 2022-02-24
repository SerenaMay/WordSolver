import string
import WordGameInput as WordGame

class WordSolver:
    # Initiate WordSolver object
    def __init__(self):
        # Open file of all 5-letter English words and move them into a list
        self.words = open("words.txt", "rt")
        self.word_list = []
        for word in self.words:
            self.word_list.append(word[:5])

        # create a WordGame object
        self.WordGame = WordGame.WordGame()

    # Try a single word against the Wordle, and modifies list accordingly
    def try_word(self, guess):
        result = self.WordGame.try_val(guess)
        print(result)

        for i in range(0, 5):
            if result[i] == "g":
                self.prune_green(guess[i], i)
            elif result[i] == "y":
                self.prune_yellow(guess[i], i)
            elif result[i] == "r":
                self.prune_red(guess[i])

    # Prunes words from list without a specific letter at an index
    def prune_green(self, green_letter, index):
        for word in self.word_list[:]:
            if green_letter != word[index]:
                self.word_list.remove(word)

    # Prunes words with specific letter at any index
    def prune_red(self, red_letter):
        for word in self.word_list[:]:
            if red_letter in word:
                self.word_list.remove(word)

    # Prunes words either without specific letters, or with specific letter at index
    def prune_yellow(self, yellow_letter, index):
        for word in self.word_list[:]:
            if yellow_letter not in word:
                self.word_list.remove(word)
            elif word[index] == yellow_letter:
                self.word_list.remove(word)

    # Return current length of word_list
    def list_length(self):
        return len(self.word_list)

    # Return current highest value word
    def get_top_word(self):
        return self.word_list[0]

# create word_finder object
word_finder = WordSolver()

# Creates variable to track number of tries it took
counter = 0

# Run word_finder loop until only one possible word is in the list with automatic game
while word_finder.list_length() != 1:
    counter += 1
    print("Try: " + word_finder.get_top_word())
    word_finder.try_word(word_finder.get_top_word())
    print(word_finder.list_length())

# Return results:
try:
    print("The word is: " + word_finder.get_top_word())
    print("Tries it took: " + str(counter))
except:
    print("The result string provided eliminates all possibilities")
