a = int(input("Enter value of first side of triangle"))
b = int(input("Enter value of second side of triangle"))
c = int(input("Enter value of third side of triangle"))
if b+c>a and a+b>c and c+a>b:
      if a==b or a==c or b==c:
            print("It is an Isoceles triangle")
      if a==b==c:
            print("It is an Equilateral triangle")
      if a!=b and b!=c and a!=c:
            print("It is a Scalene triangle")
else:
      print("It is not a triangle")
