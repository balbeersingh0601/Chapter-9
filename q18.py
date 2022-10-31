x= int(input("Enter a number"))
count = 0
a = 0
while x!=0:
    a= x%10
    x= x//10
    count +=1
print("No. of digits are", count)
y= count*10+a
print(y)