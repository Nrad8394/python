#import the complex math module
'''import cmath
import math

num = eval(input("Enter the number: "))

if type(num) is complex:
    print(cmath.sqrt(num))
else:
    print(math.sqrt(num))'''

import cmath

num = 1+2

num_sqrt = cmath.sqrt(num)
print("The square root of {0} is {1:0.3f}+ {2:0.3f}j".format(num,num_sqrt.real,num_sqrt.imag))#note