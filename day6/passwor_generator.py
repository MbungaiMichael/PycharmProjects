# generates a random password
import random
letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
          'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
          'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '?', '>', '<']
user = int(input('how many letters do you want : '))
user1 = int(input('how many numbers do you want : '))
user2 = int(input('how many symbols do you want : '))
password = []
for char in range(1, user + 1):
    password.append(random.choice(letter))
for char in range(1, user1 + 1):
    password.append(random.choice(symbols))
for char in range(1, user2 + 1):
    password.append(random.choice(numbers))
random.shuffle(password)
password_list = ""
for char in password:
    password_list += char
print(password_list)