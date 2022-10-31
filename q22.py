count=0
count1= 0
count2=0
for i in range(1,11):
    age = int(input("Enter your age in years in range(26-55)"))
    if 26<=age<=35:
        count= count+1
    elif 35<=age<=45:
        count1 += 1
    elif 46<=age<=55:
        count2 += 1
    else:
        print("Invalid input")
print("No. of people  in age group 26-35 are",count)
print("No. of people  in age group 35-45 are",count1)
print("No. of people  in age group 46-55 are",count2)