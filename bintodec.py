# converting from binary to decinal
bin = (input('enter a binary number: '))
b = len(bin) - 1
s = 0
for i in range(0, b):
    x = int(bin[i])*(2**b)
    b -= 1
    s += x
s = s + 1
print(s)