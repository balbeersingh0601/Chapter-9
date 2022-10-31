#(a)
#(b)
for i in range(1,4):
    print("* " * i)
for i in range(2,0, -1):
        print("* " * i)

n = 5
for i in range(1,n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()
n = 65
for i in range(65,70):
    for j in range(65, i+1):
        print(chr(j), end=" ")
    print()
n = 5
for i in range(1, n+1):
    for j in range(i,1,-1):
        print(j-1, end=" ")
    print()
n = 5
for i in range(0,n+1):
    for j in range(n, i,-1):
        print(j, end=" ")
    print()
n = 5
for i in range(1,n+1):
    for j in range(1, i+1):
        print(j+i, end=" ")
    print()
n = 5
for i in range(1,n+1):
    for j in range(1, n+1):
        print("* ", end=" ")
    print()
n = 5
for i in range(1,n+1):
    for j in range(n,i,-1):
        print("* ",end=" ")
    print()
n = 5
for i in range(1,n+1):
    for j in range(i,n+1):
        print(j-i,end=" ")
    print()
'''n = 65
for i in range(65,70):
    for j in range(65,i+1):
        print(chr(i),end=" ")
    print()
n = 5A
for i in range(0,n+1):
    for j in range(n,i,-1):
        print(j-i,end=" ")
    print()'''
n = 4
for i in range(2,n+1):
    for j in range(2,i):
        print(i+2, end= " ")
    print()