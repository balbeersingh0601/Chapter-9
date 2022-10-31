A= int(input("Enter a number"))
B = int(input("Enter a number"))
C= int(input("Enter a number"))
if A>B and A > C:
    print ("The largest no is ",A)
    if B>C:
        print("The next largest no is ",B)
        print("The smallest no is ", C)
    else:
        print("The next largest no is ", C)
        print("The smallest no is ", B)


if B >C and B > A:
    print("The largest no is ", B)
    if A>C:
        print("The next largest no is ",A)
        print("The smallest no is ", C)
    else:
        print("The next largest no is ", C)
        print("The smallest no is ", A)

if C>A and C>B:
    print("The largest no is ", C)
    if A>B:
        print("The next largest no is ",A)
        print("The smallest no is ", B)
    else:
        print("The next largest no is ", B)
        print("The smallest no is ", A)
