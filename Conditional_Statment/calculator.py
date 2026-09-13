a=int(input("Enter a:"))
b=int(input("Enter b:"))
operator=input("Enter operator:")

result=a+b if operator=="+" else a-b if operator=="-" else a*b if operator == "*" else a/b if operator=="/" else "Invalid operator"
print("result : ",result)