# to find multiples of a number (P9.5)
print("Enter five numbers below")
num1 = float(input("First number :"))
num2 = float(input("Second number :"))
num3 = float(input("Third number :"))
num4 = float(input("Fourth number :"))
num5 = float(input("Fifth number :"))
divisor = float(input("Enter divisor number :"))
count = 0
print("Multiples of", divisor, "are :")
remainder = num1 %divisor
if remainder == 0:
    print(num1,sep =" ")
    count += 1
remainder = num2%divisor
if remainder == 0:
    print(num2, sep =" ")
    count += 1
remainder = num3 %divisor
if remainder == 0:
    print(num3, sep =" ")
    count += 1
remainder = num4 %divisor
if remainder == 0:
    print(num4, sep =" ")
    count += 1
remainder = num5 %divisor
if remainder == 0:
    print(num5, sep =" ")
    count += 1
print()
print(count, "multiles of", divisor, "found")
