
n=int(input("Enter a perfect square number"))
a = n**(1/2)
print("Square root of entered no is ",a)
i =2
count =0
while i<=a:
    if a%i==0:
        count +=1
    i +=1
if count>1:
    print("Square root of entered number is not prime")
else:
    print("Square root of entered number is prime")
