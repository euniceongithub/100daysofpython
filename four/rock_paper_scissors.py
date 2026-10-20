import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

system_play = random.randint(0, 2)
user_play = int(input("What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors.\n"))
art_list = [rock, paper, scissors]

if user_play >= 0 and user_play < 3:
    print(f"You chose: \n {art_list[user_play]}")
print(f"Computer chose: \n {art_list[system_play]}")

if user_play == system_play:
    print("Draw. Try again.")

if user_play == 0 and system_play == 1:
    print("You lose.")

if user_play == 0 and system_play == 2:
    print("You win.")

if user_play == 1 and system_play == 0:
    print("You win.")

if user_play == 1 and system_play == 2:
    print("You lose.")

if user_play == 2 and system_play == 0:
    print("You lose.")

if user_play == 2 and system_play == 1:
    print("You win.")

if user_play < 0 or user_play >= 3:
    print("Your input is invalid. You lose.")
