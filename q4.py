import math
l = float(input("Enter the 1st no."))
b = float(input("Enter the 2nd no."))
result = l-b
print(result)
r1 = math.fabs(result)
print(r1)
if(r1 <= 0.001):
    print("Close")
else :
    print("Not Close")
