num1=int(input("Enter number 1:"))
num2=int(input("Enter number 2:"))
num3=int(input("Enter number 3:"))

if(num1>num2 and num1>num3):
    print("number 1 is larger than other 2 number")
elif(num2>num1 and num2>num3):
    print("Number 2 is larger than other 2 number")
else:
    print("Number 3 is larger than other 2 number")