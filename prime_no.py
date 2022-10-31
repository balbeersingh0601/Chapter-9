n = int(input("Enter a number"))
count = 0
i = 2
while i<=n:
    if n%i == 0:
       count += 1
    i += 1
if count>1:
    print("Not a prime number")
else:
    print("Prime")
# to print mersenne number
n = int(input("Enter a number"))
for i in range(1, n):
    m = 2**i-1
    print("Mersenne numbers are",m)
