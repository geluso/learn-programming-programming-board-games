# credit to this repo for the plain text file list of words
# https://raw.githubusercontent.com/dwyl/english-words/master/words.txt
import random

ASCII_ART_FRAMES = [
    """
  ------
 /
/
|
|
|
|
|
|
|
==========
""",
    """
  ------
 /
/
|
|
|
|
|   /
|  /
|
==========
""",
    """
  ------
 /
/
|
|    |
|    |
|    |
|   / \\
|  /   \\
|
==========
""",
    """
  ------
 /
/
|    o
|    |
|    |
|    |
|   / \\
|  /   \\
|
==========
""",
    """
  ------
 /
/
|    o
|   /|
|  | |
|    |
|   / \\
|  /   \\
|
==========
""",
    """
  ------
 /
/
|    o
|   /|\\
|  | | |
|    |
|   / \\
|  /   \\
|
==========
""",
    """
  ------
 /   |
/    |
|    o
|   /|\\
|  | | |
|    |
|   / \\
|  /   \\
|
==========
""",
    """
  ------
 /   |
/    |
|    |
|    X
|   /|\\
|   |||
|    |
|   | |
|   | |
==========
""",

]


def load_words():
    # read words from a dictionary file
    # use strip to cut off whitespace and newlines
    words = open("./words.txt").readlines()
    words = list(map(str.strip, words))
    return words


def display_word(word, guesses):
    display = ""
    for letter in word:
        if letter in guesses:
            display += letter
        else:
            display += "_"
    return display


def hangman():
    words = load_words()
    word = random.choice(words)

    # we could remove total_guesses and just use len(guesses)
    # we need to make sure not to add duplicate items to the guesses list
    guesses = []
    total_guesses = 0
    incorrect_guesses = 0

    print(ASCII_ART_FRAMES[incorrect_guesses])
    displayed_word = display_word(word, guesses)
    print(displayed_word)

    is_guessing = True
    while is_guessing:
        print("guesses:", "".join(guesses))
        print("enter a guess: ", end="")
        letter = input().strip()
        guesses.append(letter)

        total_guesses += 1
        if letter not in word:
            incorrect_guesses += 1

        print(ASCII_ART_FRAMES[incorrect_guesses])

        displayed_word = display_word(word, guesses)
        print(displayed_word)

        # you're out of guesses
        if incorrect_guesses >= len(ASCII_ART_FRAMES) - 1:
            is_guessing = False
            print("guesses:", "".join(guesses))
            print("You lost! The word was:", word)

        # you guessed the whole word
        if "_" not in displayed_word:
            is_guessing = False
            print("guesses:", "".join(guesses))
            print("You got it in", total_guesses, "guesses!")


def main():
    hangman()


main()
