# Display menu for calculating area or perimeter of circle  (P9.6)
radius = float(input("Enter radius of circle :"))
print("1. Calculate Area")
print("2. Calculate Perimeter")
choice = int(input("Enter your choice (1 or 2) :" ))
if choice == 1:
    area = 3.14159* radius *radius
    print("Area of circle with radius", radius, 'is', area)
else:
    perm = 2*3.14159 * radius
    print("Perimeter of circle with radius", radius, 'is', perm)

# to read two number and arithmetic operator and display result  (P9.7)
num1 = float(input("Enter first number"))
num2 = float(input("Enter second number"))
op = input("Enter operator[+ - * / %] :")
result = 0
if op == '+':
    result = num1 + num2
elif op == '-':
    result = num1 - num2
elif op == '*':
    result = num1 * num2
elif op == '/':
    result = num1 / num2
elif op == '%':
    result = num1 % num2
else :
    print("Invalid operator !!")
print(num1, op, num2, '=', result)