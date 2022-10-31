n = int(input("Enter number of items"))
if n<10 :
    print("Cost of", n,"items is ", n*120,"rupees")
elif (n>10 and n<99):
     print("Cost of", n,"items is ", n*100,"rupees")
if n>=100:
    print("Cost of", n,"items is ", n*70,"rupees")