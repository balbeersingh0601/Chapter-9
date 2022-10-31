import math
count =0
r = int(input("Enter the range of no"))
for num in range(4,r+1):

    while num % 2 == 0:
        print(num,"=",2,'*', end = ' ')
        num = num // 2

    for i in range(3, num+1, 2):

        # while i divides n , print i ad divide n
        while num % i == 0:
            print(num,"=",i,'*', end = ' ')
            num = num // i
            count = count +1
    if count > 2:
        print(num, "PRIME")
    print()