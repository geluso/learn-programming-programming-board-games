import random


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

    is_guessing = True
    while is_guessing:
        print("enter a guess: ", end="")
        letter = input().strip()
        guesses.append(letter)

        total_guesses += 1

        displayed_word = display_word(word, guesses)
        print(displayed_word)

        if "_" not in displayed_word:
            is_guessing = False
            print("You got it in", total_guesses, "guesses!")


def main():
    hangman()


main()
