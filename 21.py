sum = 0
for i in range(5):
    fact = 1
    for j in range(1,i+1):
        fact= fact*j
    term= (1/fact)
    sum = sum+term
print(sum)