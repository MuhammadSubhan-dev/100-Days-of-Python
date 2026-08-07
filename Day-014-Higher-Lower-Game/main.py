import art
import game_data
import random

def format_data(account):
    """Format the account data into printable data"""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"] 
    return f"{account_name}, a {account_descr}, from {account_country}."

def check_follower_count(a_followers, b_followers, user_guess):
    """Take the user's guess and follower counts and returns if they it right"""
    if a_followers > b_follower_count:
        return user_guess == "a"
    else:
        return user_guess == "b"
        
print(art.logo)
score = 0
game_should_continue = True
compare_B = random.choice(game_data.data)

while game_should_continue:
    compare_A = compare_B
    compare_B = random.choice(game_data.data)
    if compare_A == compare_B:
        compare_B = random.choice(game_data.data)

    print(f"Compare A: {format_data(compare_A)}")
    print(art.vs)
    print(f"Compare B: {format_data(compare_B)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    print("\n" * 20)
    print(art.logo)
    a_follower_count = compare_A["follower_count"]
    b_follower_count = compare_B["follower_count"]

    is_correct = check_follower_count(a_follower_count, b_follower_count, guess)

    if is_correct:
        score += 1
        print(f"You're right! Current score {score}.")
    else:
        print(f"Sorry, that's wrong. Final score {score}.")
        game_should_continue = False