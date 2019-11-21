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
  print("rock, paper, or scissors?")
  choice = input()
  print()
  return choice

def play_round():
  choices = ["rock", "paper", "scissors"]
  computer = computer_choice(choices)
  player = player_choice()

  if player not in choices:
    print("invalid input!")
    return

  # print what each player played and an empty line for spacing
  print("  player:", player)
  print("computer:", computer)
  print()

  if player == computer:
    print("tie")
  else:
    winner = determine_winner(computer, player)
    print(winner, "wins")

def main():
  play_round()
 
main()
