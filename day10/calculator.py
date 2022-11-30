
def add(n, m):
    return n + m


def subtract(n, m):
    return n-m


def multiply(n, m):
    return n * m


def divide(n, m):
    return n / m


dictionary ={
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}
calculating = True
f_number = int(input('what is the first number: '))
for key in dictionary:
    print(key)
while calculating:
    operation_symbol = input('enter an operation : ')
    l_number = int(input('what is the next number: '))
    function = dictionary[operation_symbol]
    a = function(f_number, l_number)
    print(f'{f_number} {operation_symbol} {l_number} = {a}')
    outcome = input(f"Type 'y' to continue calculating with {a} or 'n' to exit: ")
    if outcome == 'y':
        f_number = a
    else:
        calculating = False


# operation_symbol = input('pick another operation : ')
# num3 = int(input("enter another number: "))
# function = dictionary[operation_symbol]
# b = function(function(f_number, l_number), num3)
# print(f'{l_number} {operation_symbol} {num3} = {b}')
