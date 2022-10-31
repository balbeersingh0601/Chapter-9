'''N = int(input("Enter any number"))
i = 1
if N>20:
    while i <= N:
        if N % 3 == 0:
             print("Tipsy")
        if N%7 == 0:
             print("Topsy")
        if N%3 == 0 and N%7 == 0:
              print("Tipsy Topsy")
    i = i + 1
else:
    print("Entry is invalid")'''


N = int(input("Enter any number N>20"))
for i in range(11,N):
    if i%3==0:
        print("Tipsy",i)
    if i%7==0:
        print("Topsy",i)
    if i%21==0:
        print("Tipsy Topsy",i)

