# to input 3 no.s and calculate their sum  (P9.3)
sum1 = sum2 = 0
num1 = int(input("Enter number 1 :"))
num2 = int(input("Enter number 2 :"))
num3= int(input("Enter number 3:"))
sum1 = num1 + num2 + num3
if num1 == num2 :
    if num3 != num1 :
      sum2 += num3
else:
   if num2 == num3:
    sum2 += num2
   else:
         if num2 == num3:
            sum2 += num1
         else:
             sum2 += num1 +num2  + num3
print("Numbers are", num1, num2, num3)
print("Sum of three given no.s is",  sum1)
print("Sum of non-duplicate numbers is", sum2)

# to test if a no. is divisible by another no (P9.4).

number1 = int(input("Enter first number"))
number2 = int(input("Enter second number"))
remainder = number1% number2
if remainder == 0:
    print(number1, "is divisible by", number2)
else:
    print(number1, "is not divisible by", number2)

