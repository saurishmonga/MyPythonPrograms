n=input("Enter Character: ")
if(n>='a') and (n<='z'):
    print(n, "is an alphabet")
elif(n>='A') and (n<='Z'):
    print(n, "is an alphabet")
elif(n>='0') or (n<='9') or (n<='0'):
    print(n, "is a number")
else:
    print(n, "is a special character")
    
