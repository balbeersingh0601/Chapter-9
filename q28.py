temp=float(input("Enter temperature "))
unit=input("Enter unit in celsius or fahrenheit")
if unit=="celsius" or unit=="Celsius":
    F = 9/5*temp +32
    print(" Converted Temperature in Fahrenheit is",F)
elif unit=="fahrenheit" or unit=="Fahrenheit":
    C = 5/9*temp -32
    print(" Converted Temperature in Celsius is", C)
else:
    print("Write the unit correctly")