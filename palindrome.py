# to find palindrome
rev = 0
a = 0
n = int(input("Enter a number"))
input = n
while n!= 0 :
    a = n%10
    n = n//10
    rev = rev*10+a
if rev == input:
    print("Palindrome number")
else:
    print("Not a Palindrome number")

