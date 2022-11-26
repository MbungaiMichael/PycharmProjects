# caesar cipher program
# to encrypt and decrypt

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

Direction = input("Type 'encode' to encrypt and 'decode' to decrypt:\n").lower()
Text = input('Enter your message:\n').lower()
Shift_num = int(input('insert the shift number:\n'))


def caesar(shift, direction, text):
    stringing = ""
    for i in text:
        position = alphabet.index(i)
        if direction == 'decode':
            shift *= -1
        new_position = position + shift
        new_i = alphabet[new_position]
        stringing += new_i
    print(f"The {direction}d word is {stringing}")


caesar(shift=Shift_num, direction=Direction, text=Text)