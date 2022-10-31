# to read 3 no.s and print them in ascending order (P9.8)
x = int(input("Enter first number :"))
y = int(input("Enter second number :"))
z = int(input("Enter third number :"))
min = mid = max

if x<y and x<z :
    if y<z :
        min, mid, max = x, y, z
    else:
        min, mid, max = x, z, y
elif y<x and y<z :
    if x<z:
        min, mid, max = y, x, z
    else:
        min, mid, max = y, z, x
else:
    if x<y:
        min, mid, max = z, x, y
    else:
        min, mid, max = z, y, x
print("Numbers n ascending order :",  min, mid, max )

#to print sum of natural no.s between 0 to 7  (P9.13)
sum = 0
for n in range(1, 8):
    sum += n
print("Sum of natural numbers <=", n, 'is', sum)
