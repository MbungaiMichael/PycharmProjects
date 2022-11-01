# converting from a decimal number to binary
dec = int(input('enter a non negative integer: '))
s = ''
demo = dec
while demo != 0:
    y = demo % 2
    demo = demo // 2
    s = str(y) + s
print(s)