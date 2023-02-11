from tkinter import *


root = Tk()
root.title("Mile to kilometer converter")
root.minsize(width=200, height=150)
root.config(padx=30, pady=30)

# label
miles_label = Label(text="Miles", font=("Arial", 15, "normal"))
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to ", font=("Arial", 15, "normal"))
is_equal_label.grid(column=0, row=1)

km_label = Label(text="km", font=("Arial", 15, "normal"))
km_label.grid(column=2, row=1)
my_label = Label()



def converter():
    """  Converting miles to kilometer """
    number = float(int(input.get()) / 0.621)
    my_label.config(text=number, font=("Arial", 15, "normal"))
    my_label.grid(column=1, row=1)


# button
button = Button(text="Calculate", command=converter)
button.grid(column=1, row=2)

# enter
input = Entry(width=30)
input.grid(column=1, row=0)

# text
# ttt

root.mainloop()
