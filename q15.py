print("Finding largest numbers from the list of five no, ")
n1 = int(input("Enter a number"))
max=n1
for i in range(1,5):
    n = int(input("Enter a number"))
    if n>max:
        max=n
print("Largest no. is",max)

