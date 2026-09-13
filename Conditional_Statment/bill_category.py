bill=int(input("Enter Electrivty Bill:"))

if(bill<=100 and bill>=0):
    print("Low")
elif(bill<=300 and bill>=101):
    print("Medium")
else:
    print("High")