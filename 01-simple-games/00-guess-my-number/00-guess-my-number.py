import math
import random


def pluralize(count, word, plural):
    if count == 1:
        return word
    return plural


def main():
    range_ = 100
    choice = math.floor(range_ * random.random())

    print("I'm thinking of a number between 1 and", range_)

    total_guesses = 0
    is_guessing = True

    while is_guessing:
        print("guess: ", end="")
        guess = int(input())

        total_guesses += 1

        if guess == choice:
            print("correct!")
            is_guessing = False
        elif guess < choice:
            print("higher")
        elif guess > choice:
            print("lower")

    word = pluralize(total_guesses, "guess", "guesses")
    print("you got it in", total_guesses, word)


main()
