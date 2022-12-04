import random
should_continue = True
while should_continue:
    numbers = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    users = random.choice(numbers)
    s_users = random.choice(numbers)
    user = [users, s_users]
    print(f"user = {user}")
    computer1 = random.choice(numbers)
    computer2 = random.choice(numbers)
    computer = [computer1, computer2]
    print(f"computer = {computer}")
    a = users + s_users
    b = computer1 + computer2
    if b == 21 and a == 21:
        print("The computer has a blackjack , computer wins")
    elif a == 21:
        print("The user has a blackjack , user wins")
    elif b == 21:
        print("The computer has a blackjack , computer wins")
    elif a > 21:
        for value in user:
            val = value
            if val == 11:
                num = user.index(val)
                user[num] = 1
        print("The user is burst,the user losses")
    res = input("user, do you want another card 'y' for yes or 'n' for no : ")
    if res == 'y':
        user1 = random.choice(numbers)
        a += user1
    if b <= 16:
        computer3 = random.choice(numbers)
        b += computer3
