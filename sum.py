# print sum of  n natural numbers
n = int(input("Enter a number"))
i = 1
sum = 0
while i<=n:
    sum = sum+i
    i +=1
print("Sum of",n,"natural numbers is",sum)
# to find factorial
n = int(input("Enter a number"))
i = 1
fact = 1
while i<=n:
    fact= fact*i
    i +=1
print("Factorial of",n, "are", fact)
