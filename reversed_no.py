# to print reversed number
a = 0
n = int(input("Enter a number"))
while n!=0:
    a = n%10
    n = n//10
    print(a,end='')

