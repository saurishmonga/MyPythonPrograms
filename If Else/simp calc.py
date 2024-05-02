num=float(input("Enter a Number: "))
num2=float(input("Enter the second number: "))
calc=input("Enter an operator: ")
if(calc=='+'):
    print(num+num2)
elif(calc=='-'):
    print(num-num2)
elif(calc=='*'):
    print(num*num2)
elif(calc=='/'):
    print(num/num2)
else:
    print("Invalid Operator")
    
