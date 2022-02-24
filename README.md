A program to solve popular 5-letter word games.

To run:
have WordSolver.py and either WordGame classes in same directory, with a list of 5-letter words (with each word on
  its own line) titled "words.txt" in the same directory (lists can be found easily by a Google search, or
    here: https://www-cs-faculty.stanford.edu/~knuth/sgb-words.txt)
When this is done, simply run "python WordSolver.py"

To select between the Automatic and Input versions:
Change line 2 of WordSolver.py to reflect proper import

The automatic version runs the game automatically, selecting a secret word and testing the
selected word against it

The input version has the user input the selected word into their perferred 5-letter
word game (such as the NYT Wordle game), and have respond with how it fared.

NOTE: In traditional 5 letter word games, with duplicate letters tried, if there is only one in the word,
the game will show it as one being yellow, and the other "red" or greyed out.
Here, show both copies of the letter as yellow.
