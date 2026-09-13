a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=int(input("Enter c:"))
largest= a if a>=b and a>=c else b if b>=c else c 
print("Largest Number is:",largest)