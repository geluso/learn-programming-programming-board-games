import math
import random


def is_winner(player, opponent):
    # this could be written as one long combined if statement.
    # I personally prefer to write lots of small pieces of logic.
    # I find this gives me more places to inspect and debug the program,
    # especially as programs and logic become more complex.
    if player == "rock" and opponent == "scissors":
        return True
    elif player == "paper" and opponent == "rock":
        return True
    elif player == "scissors" and opponent == "paper":
        return True

    # if they didn't win they didn't win!
    return False


def determine_winner(computer, player):
    if computer == player:
        return "tie"
    elif is_winner(player, computer):
        return "player"
    elif is_winner(computer, player):
        return "computer"


def computer_choice(choices):
    choices = ["rock", "paper", "scissors"]
    choice = random.choice(choices)
    return choice

# prompt for user input and print an empty line to add spacing


def player_choice():
    print()
    print("rock, paper, or scissors? (or 'exit')")
    choice = input()
    print()
    return choice


def play_round():
    choices = ["rock", "paper", "scissors"]
    computer = computer_choice(choices)
    player = player_choice()

    if player == "exit":
        return "exit"

    if player not in choices:
        print("invalid input!")
        return

    # print what each player played and an empty line for spacing
    print("  player:", player)
    print("computer:", computer)
    print()

    if player == computer:
        print("tie")
        return "tie"
    else:
        winner = determine_winner(computer, player)
        print(winner, "wins")
        return winner


def rock_paper_scissors(rounds_to_win):
    player_score = 0
    computer_score = 0

    is_playing = True
    while is_playing:
        result = play_round()

        # check for quit
        if result == "exit":
            is_playing = False

        # increment appropriate scores
        if result == "player":
            player_score += 1
        elif result == "computer":
            computer_score += 1

        print()
        print("  player score:", player_score)
        print("computer score:", computer_score)

        if player_score >= rounds_to_win:
            return "player"
        elif computer_score >= rounds_to_win:
            return "computer"


def main():
    print("Rock! Paper! Scissors!")
    print("Best of how many rounds? (default 5)")
    rounds = 5

    input_ = input()
    if input_ != "":
        rounds = int(input_)

    # the first player to win the majority of rounds wins
    rounds_to_win = math.ceil(rounds / 2)
    print("Playing best", rounds_to_win, "out of", rounds)

    winner = rock_paper_scissors(rounds_to_win)
    print(winner, "wins")


main()
