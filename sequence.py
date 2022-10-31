# print seq (5, -10, 15, -20)
sign = 1
for i in range(5, 21, 5):
    r = sign*i
    print(r)
    sign = sign* -1
# print square of seq (5, -10, 15, -20)
sign = 1
for i in range(5, 21, 5):
    r = sign*i*i
    print(r)
    sign = sign* -1

for i in range(4, 0, -1):
    for j in range(4, i-1, -1):
        print(j, end=' ')
    else:
        print()
for i in range(5):
    for j in range(1, i+1):
        print(j, end=' ')
    else:
        print()
first = 0
second = 1
for i in range(1,11):
    print(first)
    third = first+second
    first, second= second, third
n = int(input("Enter a number"))
i = 1
sum = 0
while i<n:
     if (n%i==0):
         sum = sum+i
     i +=1
print(sum)
if sum==n:
    print("Perfect number is",sum)
else:
   print("Not a perfect number")
n = int(input("Enter a number"))
for i in range(n):
    for j in range(i,-1,-1):
        print(i+2,end=" ")
    print()
n = int(input("Enter a number"))
for i in range(n):
    for j in range(i,2):
        print(i+2,end=" ")
    print()


