mark=int(input("Enter your marks:"))

if(mark>=80):
    print("A+")
elif(mark>=70 and mark<80):
    print("A")
elif(mark>=60 and mark<70):
    print("B")
elif(mark>=50 and mark<60):
    print("C")
else:
    print("F")