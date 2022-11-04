import random

word_list = ['advocate', 'principal', 'jurisdiction', 'empathy']
chosen_word = random.choice(word_list)
print(chosen_word)
a = 0
start = 0
display = []

for i in chosen_word:
    display.append("_")
while a != 1:
    user_input = input('enter a letter of your choosing: ').lower()
    for i in range(len(chosen_word)):
        letter = chosen_word[i]
        if letter == user_input:
            display[i] = letter
    print(display)
    if "_" not in display:
        a = 1
        print("You win")