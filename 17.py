n = int(input("Enter a number"))
input = n
rev = 0
while n!=0:
    a = n%10
    n = n//10
    rev = rev*10+a
if rev== input :
    print("It is a Palindrome number")
else:
    print("It is  not a Palindrome number")