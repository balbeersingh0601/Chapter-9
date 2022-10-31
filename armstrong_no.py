# Armstrong number
n = int(input("Enter a number"))
input = n
a = 0
i = 1
rs = 0
while i<=n:
    a = n%10
    n = n//10
    rs = rs+a*a*a
if rs == input:
    print("Armstrong number")
else:
    print("Armstrong number")