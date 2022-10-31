def level():
    print('Welcome to the magic number game,there are 4 levels of the game: \n'
          '1.Extreme - 3 points(attempts)\n'
          '2.Difficult - 5 points(attempts)\n'
          '3.Medium - 10 points(attempts)\n'
          '4.Easy - 15 points(attempts)\n')
    u = int(input('choose your level: '))
    if u == 1:
        return 3
    elif u == 2:
        return 5
    elif u == 3:
        return 10
    elif u == 4:
        return 15

