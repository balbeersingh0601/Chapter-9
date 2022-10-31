# Check odd or even number (P9.1)
'''num = int(input("Enter an integer"))
if num % 2 == 0:
    print(num, "is Even number.")
else:
    print(num, "is ODD number")
    '''
# to print largest of three integers (P9.2)
x = y = z = 0
x = float(input("Enter first number"))
y = float(input("Enter second number"))
z = float(input("Enter third number"))

max = x
if y > max:
    max = y
if z > max:
    max = z
print("Largest number is ", max)
