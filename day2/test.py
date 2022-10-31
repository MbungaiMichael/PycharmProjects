
print(' ========================================================\n'
      ' =                                                      =\n'
      ' =          Welcome to the treasure island.             =\n'
      ' ========================================================\n'
      '    you are to find the treasure in a mysterious island   \n'
      " You're start point is at a cross road, do you want to take left or right ?")
user = input().lower()
if user == 'right':
    print('Game Over')
elif user == 'left':
    print('You have arrived at a dangerous river ,do you wmt to swim or wait')
    user1 = input().lower()
    if user1 == 'swim':
        print('Game Over, try again')
    elif user1 == 'wait':
        print("A stranger passed by and saved you on a boat.you successfully crossed the bass mouth village\n "
              "and headed for the mountain and there are a light of different colour at the end of each tunnel.\n"
              "there is red,blue and yellow lights. which tunnel light will you choose? \n")
        user2 = input().lower()
        if user2 == 'red' or "blue":
            print('Game Over')
        else:
            print('you have found the treasure.you have won .')
