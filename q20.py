'''n1 = int(input("Enter a number"))
sum = 0
for i in range(1,n1+1):
    sum = sum+i*i
print("Sum of the sequence is 1^2  +2^2 + 3^2.............n^2",sum)'''
#(b)
sign = 1
num=2
den=9
i=1
term =0
sum = 0
while i<=3:
    term = (num/den)*sign
    sum += term
    i = i+1
    sign = sign*-1
    num +=3
    den +=4
print(sum)

