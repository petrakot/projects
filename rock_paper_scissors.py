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

#Write your code below this line 👇

user_choice = input("What do you chose? Type 0 for rock, 1 for paper and 2 for scissors.\n")
new_user_choice = int(user_choice)

choice = [rock, paper, scissors]
computer_choice = random.randint(0,2)

print(f"You chose \n {choice[new_user_choice]},\nThe computer choce,\n {choice[computer_choice]}")

if new_user_choice == computer_choice:
  print("You are even!")
else:
  if new_user_choice > computer_choice:
    if new_user_choice == 1:
      print("You win!")
    elif new_user_choice == 2:
      if computer_choice == 1:
        print("You win!")
      else:
        print("You lost!")
    elif new_user_choice == 0:
      if computer_choice == 1:
        print("You lost!")
      else:
        print("You won!")
  else:
    if new_user_choice == 1:
      print("You win!")
    elif new_user_choice == 2:
      if computer_choice == 1:
        print("You win!")
      else:
        print("You lost!")
    elif new_user_choice == 0:
      if computer_choice == 1:
        print("You lost!")
      else:
        print("You won!")
