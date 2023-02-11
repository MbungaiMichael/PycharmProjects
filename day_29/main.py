from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json
# import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def password_generator():
    letters = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]
    symbols = ['~', '!', '!', '@', '#', '$', '%', '^',
               '&', '*', '(', ')', '_', '+', '?', '>',
               '<', ':', '"', '}', '{', '|', '/', '.',
               ',']
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    generated_password = []
    gen = [generated_password.append(choice(letters)) for char in range(randint(4, 6))]
    gen_2 = [generated_password.append(choice(symbols)) for i in range(randint(2, 4))]
    gen_1 = [generated_password.append(choice(numbers)) for cha in range(randint(2, 4))]

    shuffle(generated_password)
    password_gen = ""

    for char in generated_password:
        password_gen += str(char)
    password_entry.insert(0, f'{password_gen}')
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    new_dic = {
        website: {
            'email': email,
            'password': password,
        }
    }
    if len(website) > 0 and len(password) > 0:
        with open('data.json', 'w') as data_f:
            json.dump(new_dic, data_f)
            website_entry.delete(0, END)
            password_entry.delete(0, END)
    else:
        oops = messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!!")


# -----y----------------------- UI SETUP ------------------------------- #
root = Tk()
root.title("Password Manager")
root.minsize(width=450, height=450)
root.config(padx=50, pady=50)

# label
website_label = Label(text="Website:")
website_label.grid(column=0, row=2)

email_label = Label(text="email/Username:")
email_label.grid(column=0, row=3)


password_label = Label(text="Password:")
password_label.grid(column=0, row=4)

# entry
website_entry = Entry(width=35)
website_entry.grid(column=1, row=2, columnspan=2)
website_entry.focus()


email_entry = Entry(width=35)
email_entry.grid(column=1, row=3, columnspan=2)
email_entry.insert(0, "michaelmbungai@gmail.com")

password_entry = Entry(width=20)
password_entry.grid(column=1, row=4,  columnspan=1)

# button
generate_password = Button(text="Generate Password", command=password_generator, width=14)
generate_password.grid(column=2, row=4, columnspan=1)

add_button = Button(text="Add", command=save_password, width=35)
add_button.grid(column=1, row=5, columnspan=2)

canvas = Canvas(width=201, height=190, highlightthickness=0)
photoImage = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=photoImage)
canvas.grid(column=1, row=0)



root.mainloop()
