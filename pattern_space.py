'''
n=5
for i in range (1,n+1):
    for space in range(i,n):
        print('*', end =' ')
    for j in range(1,i+1):
        print('@', end=" ")
    print()

n=5
for i in range (1,n+1):
    for space in range(i,n):
        print(' ', end =' ')
    for j in range(1,i+1):
        print('@', end=" ")
    print()
'''
n=5
for i in range (1,n+1):
    for space in range(i,n):
        print(' ', end =' ')
    for j in range(i+1,0):
        print(j, end=" ")
    print()
