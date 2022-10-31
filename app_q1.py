'''count=0
a=None
if(a==0):
    print("Zero")
    count+=1
if(a==1):
    print("One")
    count+=1
if(a==2):
    print("Two")
    count+=1
if(a==3):
    print("Three")
    count+=1
print("The no. of comparisions is ",count)
count=0
for a in range(0,4):
    if (a == 0):
        print("Zero")
        count += 1
    if (a == 1):
        print("One")
        count += 1
    if (a == 2):
        print("Two")
        count += 1
    if (a == 3):
        print("Three")
        count += 1
print("The no. of comparisions is ",count)'''

#Q2
temp = int(input("Enter the value to temp to print water"))
if(temp< 32):
    print("ice")
elif(temp <212):
    print("water")
else:
    print("steam")

