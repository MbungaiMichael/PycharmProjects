# caesar cipher program
# to encrypt and decrypt in one function

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# using three parameters shift,direction and text.
# we get the text and shift by a certain number for encoding and vice versa for decoding.


def caesar(shift, direction, text):
    stringing = ""
    if direction == 'decode':
        shift *= -1
    for i in text:
        if i in alphabet:
            position = alphabet.index(i)
            new_position = position + shift
            stringing += alphabet[new_position]
        else:
            stringing += i
    print(f"The {direction}d word is {stringing}")


should_start = True
while should_start:
    Direction = input("Type 'encode' to encrypt and 'decode' to decrypt:\n").lower()
    Text = input('Enter your message:\n').lower()
    Shift_num = int(input('insert the shift number:\n'))
    Shift_num = Shift_num % 26

    caesar(shift=Shift_num, direction=Direction, text=Text)
    con = input("do you want to continue 'yes' or 'no': ").lower()
    if con == 'no':
        should_start = False
        print('goodbye...')
