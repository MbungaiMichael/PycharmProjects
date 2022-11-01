# if number is divisible by 3 & 5,or only 3 or only 5
print('Enter a number :')
user = int(input())
if (user % 3) ==0 and (user % 5) == 0:
    print("fissbuzz")
elif (user % 3) == 0 :
    print('fiss')
elif (user % 5) == 0:
    print('buzz')
else:
    print('Not divisble')