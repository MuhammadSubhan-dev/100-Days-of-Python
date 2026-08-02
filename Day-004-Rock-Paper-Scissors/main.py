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

print("______________ Rock Paper Scissors ______________")
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
if user_choice < 0 or user_choice > 2:
    print("Invalid choice. You lose!")
else:
    print("You chose:")
    if user_choice == 0:
        print(rock)
    elif user_choice == 1:
        print(paper)
    else:
        print(scissors)

    print("Computer chose:")
    random_choice = random.randint(0, 2)

    if random_choice == 0:
        print(rock)
    elif random_choice == 1:
        print(paper)
    else:
        print(scissors)

    if user_choice == random_choice:
        print("Draw")
    elif (
        (user_choice == 0 and random_choice == 2)
        or (user_choice == 2 and random_choice == 1)
        or (user_choice == 1 and random_choice == 0)
    ):
        print("You Win!")
    else:
        print("You Lose!")