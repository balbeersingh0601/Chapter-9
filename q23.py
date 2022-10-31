#(a)
x = int(input("Enter a number"))
sum = 0
sign=1
for i in range(1,5):
    fact=1
    for j in range(1,i+1):
        fact= fact*j
    term = ((x**i)*sign)/fact
    sum += term
    sign= sign*-1
print(sum)

#(b)
x = int(input("Enter a number"))
n = int(input("Enter a number"))
sum = 0
for i in range(1,5):
    term = (x**i)//i
    sum += term
print(sum)
