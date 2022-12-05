import random
from replit import clear


def deal_card():
    """  returns a number from the deck"""
    numbers = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(numbers)
    return card


def calc_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "it's a draw"
    elif computer_score == 0 :
        return "you lose,the computer has a blackjack"
    elif user_score == 0 :
        return "you win,you have a blackjack"
    elif user_score > 21:
        return "you lose,the computer has won"
    elif computer_score > 21:
        return "you win"
    elif user_score > computer_score:
        return "you win"
    else:
        return "you lose,the computer has won"


def play_game():
    s_users = []
    computer = []
    is_game_over = False
    for number in range(2):
        s_users.append(deal_card())
        computer.append(deal_card())
    while not is_game_over:
        user_score = calc_score(s_users)
        computer_score = calc_score(computer)
        print(f" your score :{s_users}, current score : {user_score}")
        print(f" computer's score :{computer[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_continue = input("type 'y' o continue or 'n' to stop: ").lower()
            if user_should_continue == 'y':
                s_users.append(deal_card())
            else:
                is_game_over = True

    while computer_score < 17 and computer_score !=0:
        computer.append(deal_card())
        computer_score = calc_score(computer)
    print(f"your score :{s_users}, final score : {user_score}")
    print(f"computer's score :{computer},final score : {computer_score}")
    print(compare(user_score, computer_score))


while input("do ou want to play blackjack,type 'y' for yes or 'n' for no : ").lower() == 'y':
    clear()
    play_game()