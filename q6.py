'''a = int(input("Enter the 1st side"))
b = int(input("Enter the 2nd side"))
c = int(input("Enter the 3rd side"))
if a+b>c:
    if b+c>a:
       if c+a>b:
           print("It is a triangle")
       else:
           print("It is not a triangle")
    else:
        print("It is not a triangle")
else:
    print("It is not a triangle")'''

a = int(input("Enter the 1st side"))
b = int(input("Enter the 2nd side"))
c = int(input("Enter the 3rd side"))
if b+c>a and a+b>c and c+a>b:
    print("It is a triangle")
else:
    print("It is not a triangle")
