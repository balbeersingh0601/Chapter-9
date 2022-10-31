n = int(input("Enter the range (1-n)")) # Let suppose u add the range 1-100
m = int(input("Enter the number")) # Let suppose u enter the no. 5 to check the divisibility
for i in range(1,n):
    if i%m==0:
        if i%2==0:
            print(i," is even")
        else:
            print(i," is odd")

