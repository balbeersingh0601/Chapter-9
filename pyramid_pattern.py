#1
'''for i in range(1,6):
    print("*" * i)
#2
for i in range(5,0, -1):
    print("*" * i)'''
#3
rows = 5
k = 2 * rows - 2
for i in range(0, rows):
     for j in range(0, k):
         print(end = " ")
     k = k - 2
     for j in range(0, i + 1):
         print("* ", end="")
     print("")
#4
rows = 6
for i in range(1, rows):
    num = 1
    for j in range(rows,0, -1):
        if j > i:
            print(" ", end = ' ')
        else:
            print(num, end = ' ')
            num += 1
    print("")
