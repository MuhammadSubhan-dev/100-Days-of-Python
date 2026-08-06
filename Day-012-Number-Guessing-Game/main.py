import art
import random


def generate_random_number():
    random_number = random.randint(1, 100)
    return random_number

guess_correct = False
print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
number = generate_random_number()

if difficulty == 'easy':
    guess_limit = 10
else:
    guess_limit = 5

while guess_limit > 0 and not guess_correct:
    print(f"You have {guess_limit} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))

    if guess == number:
        guess_correct = True
        print("You got it! The number was " + str(number))
    elif guess > number:
        print("Too high!")
        guess_limit -= 1
    elif guess < number:
        print("Too low!")
        guess_limit -= 1
    if guess_limit <= 0:
        print("You ran out of guesses, you lose.")