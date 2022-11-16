#area of a triangle is 0.5*base*height
#but using heron's formular is s=(a+b+c)/2 then (s*(s-a)*(s-b)*(s-c))
method = input("Enter the area calculation method: \na)Normal method\nb)Heron'sFormula\n  ")

if method.lower() == "a":
    height = eval(input("Enter the triangle's height: "))
    base = eval(input("Enter the triangle's base: "))
    print("The area of triangle(height = {0}cm and base = {1}cm) is {2}cm".format(height,base,0.5*base*height))
else:
    a = eval(input("Enter the triangle's first side: "))
    b = eval(input("Enter the triangle's second side: "))
    c = eval(input("Enter the triangle's third side: "))
    s=(a+b+c)/2
    area = (s*(s-a)*(s-b)*(s-c))
    print("The area of triangle(side1 = {0}cm , side2 = {1}cm and side3 = {2}cm  is {3}cm".format(a,b,c,area))