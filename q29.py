temp = float(input("Enter temperature in celsius"))
if (temp<-273.15):
    print("Temperature is invalid")
elif (temp==-273.15):
    print("Temperature is absolute zero")
elif (-273.15<temp<0):
    print("Temperature is below freezing")
elif temp==0:
    print("Temperature at freezing point")
elif 0<temp<100:
    print("Temperature is in normal range ")
elif temp==100:
    print("Temperature at boiling point")
elif temp>100:
    print("Temperature above boiling point")
