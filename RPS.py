# Rock Paper scissors
import random
game_on = True
#input
user_input = input("Enter ur choice").lower()
possible_outcomes = ["rock","paper","scissors"]
computer_input = random.choice(possible_outcomes)
print(f"user : {user_input} \ncomputer : {computer_input}")

#outcomes
if user_input == computer_input:
  print("Its a tie")
elif user_input == "rock":
  if computer_input == "scissor":
    print("You win")
  else:
    print("You lost")
elif user_input == "paper":
  if computer_input == "scissors":
    print("You win")
  else:
    print("you lost")
elif user_input == "scissors":
  if computer_input == "paper":
    print("You win")
  else:
    print("you lost")
else:
  print("invalid entry")  