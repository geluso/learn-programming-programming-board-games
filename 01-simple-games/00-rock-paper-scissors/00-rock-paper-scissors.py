import random

def play_round(computer, player):
  # print what each player played and an empty line for spacing
  print("computer:", computer)
  print("  player:", player)
  print()

  if computer == player:
      return "tie"
  elif computer == "rock" and player == "scissors":
    return "computer wins"
  elif computer == "paper" and player == "rock":
    return "computer wins"
  elif computer == "scissors" and player == "paper":
    return "computer wins"
  elif player == "rock" and computer == "scissors":
    return "player wins"
  elif player == "paper" and computer == "rock":
    return "player wins"
  elif player == "scissors" and computer == "paper":
    return "player wins"

def main():
  choices = ["rock", "paper", "scissors"]
  computer_choice = random.choice(choices)

  # prompt for user input and print an empty line to add spacing
  print("rock, paper, or scissors?")
  user_choice = input()
  print()

  if user_choice in choices:
    result = play_round(computer_choice, user_choice)
    print(result)
  else:
    print("invalid input!")

main()
