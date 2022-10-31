#app_14
while True:
    n =  int(input("Enter a int:"))
    if n ==1:
        continue
    elif n ==2:
        break
    else:
        print("what")
print("Ever")

#app_12
count =0
for i in range(4):
    for j in range(5):
        if i+1 == j or j+i ==4:
            print("+", end= " ")
            count+=1
        else:
            print("o",end= " ")
print(count)