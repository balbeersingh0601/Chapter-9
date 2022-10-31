
'''weather = 'raining'
if weather=='sunny':
    print("wear sunblock")
elif weather =="snow":
    print("going skiing")
else:
    print(weather)

if int('0') == 0 :
    print("zero")
if str(0) =='zero':
    print(0)
if str(0) =='0':
    print(str(0))
else:
    print("none of the above")'''

num = int(input("Please enter a number"))
fact = 1
a = 1
while a<= num:
    fact *= a
    a += 1
print("The factorial of", num, "is", fact)