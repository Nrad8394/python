#to solve a quadratic equation =  -b-sqrt((b**2)-(4*a*c)/(2*a)) or -b+sqrt((b**2)-(4*a*c)/(2*a))
import cmath
print("---Enter the values of a,b and c---")
a = eval(input("Enter a: "))
b = eval(input("Enter b: "))
c = eval(input("Enter c: "))

#we will put the discriminant into var d

d = (b**2)-(4*a*c)

print("Your first solution is {0} and the second solution is {1} ".format((-b-cmath.sqrt(d))/(2*a),(-b+cmath.sqrt(d))/(2*a)))