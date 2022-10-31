# (a)
count = 0
while count < 10:
    print("Hello")
    count += 1
# (b)
x = 10
y = 0
while x > y:
    print(x, y)
    x = x - 1
    y = y + 1
# (c)
'''keepgoing = True
x = 100
while keepgoing:
    print(x)
    x = x - 10
    if x < 50:
        keepgoing = False
# (d)
x = 45
while x< 50 :
    print(x)
#(e)
for x in [1,2,3,4,5]:
    print(x)
#(f)
for x in range(5):
    print(x)
#(g)
for p in range(1, 10):
    print(p)
#(h)
for q in range(100,50,-10):
    print(q)
#(i)
for z in range(-500,500, 100):
    print(z)
# (j)
for y in range(500, 100, 100):
    print( y)
#(k)
x = 10
y = 5
for i in range(x-y * 2):
    print("%", i)
#(l)
for x in [1,2,3]:
    for y in [4,5,6]:
        print(x, y)
#(m)
for x in range(3):
    for y in range(4):
        print(x, y, x+y)'''
#(n)
c = 0
for x in range(10):
    for y in range (5):
        c += 1
print(c)