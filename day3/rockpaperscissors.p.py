import random

print('wha do you choose? , Type \n'
      '0 --- Rock\n'
      '1 --- paper\n'
      '2 --- scissors.')
user_input = int(input())
comp_choice = random.randint(0,2)
print(comp_choice)
if user_input == comp_choice:
    print('There is a draw')
elif user_input > comp_choice:
    print('You won')
elif user_input == 0 and comp_choice == 2:
    print('You won')
else:
    print('You lost')