from data import data
import random
from replit import clear

print("welcome to the higher or lower game")


def format_data(account):
    """convert data into a printable"""
    account_n = account['name']
    account_desc = account['description']
    account_country = account['country']
    return f"{account_n} a {account_desc} from {account_country}"


def check_answer(guess, a_account_followers, b_account_followers):
    """" comparing a and b to get the higher"""
    if a_account_followers > b_account_followers:
        return guess == "a"
    else:
        return guess == "b"


score = 0
game_shld_continue = True
account_b = random.choice(data)
while game_shld_continue:
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"compare A:{format_data(account_a)}")
    print(f"against B:{format_data(account_b)}")

    user_input = input("who has more followers? A or B : ").lower()
    a_account_followers = account_a['follower_count']
    b_account_followers = account_b['follower_count']
    is_correct = check_answer(user_input, a_account_followers, b_account_followers)

    clear()

    if is_correct:
        score += 1
        print(f"You're right, current score {score}")
    else:
        game_shld_continue = False
        print(f"Sorry that's wrong.Final score {score}")
