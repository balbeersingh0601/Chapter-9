h = int(input("Enter hour between 1-12"))
n = int(input("How many hours ahead ?"))
result = h+n
if(result >12):
    result = result -12
    print("Time at that time would be : ",result,"O'clock")
else
    print("Time at that time would be : ",result,"O'clock")