# to print fibonaci series
first = 0
second = 1
for i in range(1,10):
    print(first)
    third = first +second
    first, second = second, third
print(third)

# to  find divisors
n = int(input("Enter a number"))
i = 2
while i<=n:
    if n%i==0:
        print("Divisors of", n,"are",i)
    i = i+1
