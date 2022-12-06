import random
print("Welcome to the guessing number game")
print("I'm a number between 0 and 100 ")
user_choice = input("choose level: ").lower()


def guess(user):
    numbers = random.choice(range(0, 101))
    print(numbers)
    # if the number is 10
    if user == 'easy':
        count = 10
    elif user == 'hard':
        count = 5
    print(f"you have {count} attempts to guess the number")
    game_is_over = False
    while count != 0:
        user_guess = int(input("Make a guess: "))
        count -= 1
        if user_guess == numbers:
            print(f"you guessed the correct number which was {user_guess}")
            print(f"you have {count} attempts remaining to guess the number")
        elif user_guess > numbers:
            print(f"Too high")
            print(f"you have {count} attempts remaining to guess the number")
        else:
            print("Too low")
            print(f"you have {count} attempts remaining to guess the number")
    result = input("do you want to start the game 'y' for yes or 'n' for no: ")
    if result == 'y':
        guess(user_choice)


guess(user_choice)