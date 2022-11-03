import math
from math import sqrt
import cmath
# solving a quadratic equation
# take in the coefficients first a,b and c
# quadratic formula -b +-(b**2-4ac)/2a
# possible situations
# when there is no solution hence
def quad():
    a = int(input('enter the value of the first coefficient,a: '))
    b = int(input('enter the value of the second coefficient,b: '))
    c = int(input('enter the value of the third coefficient,c: '))
    discriminant = b**2 - 4*a*c
    if a == 0:
        print('This is not a quadratic equation')
        quad()
    if discriminant > 0:
        print("roots are real and distinct")
        x1 = (-b + math.sqrt(discriminant))/2*a
        x2 = (-b - math.sqrt(discriminant))/2*a
        print(f'the roots of the equation are {x1} and {x2}')
    elif discriminant == 0:
        print("roots are real and equal")
        x = (-b + math.sqrt(discriminant))/2*a
        print(f"The roots of the equation are {x}")
    else:
        print("the roots of the equation are imaginary")
        x1 = (-b + cmath.sqrt(discriminant))/2*a
        x2 = (-b - cmath.sqrt(discriminant))/2*a
        print(f"the roots of the equation are {x1} and {x2}")

quad()