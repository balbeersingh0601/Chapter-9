sum = 0
x = int(input("How many numbers to find average - RANGE"))
for i in range(1,x+1):
    n = int(input("Enter a number"))
    sum = sum +n
avg = sum//x
print("Average is ", avg)