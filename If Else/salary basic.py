sal=float(input("Enter the basic salary: ")) 
hra1=20/100*sal
da1=80/100*sal
sum=hra1+da1+sal
hra2=25/100*sal
da2=90/100*sal
sum1=hra2+da2+sal
hra3=30/100*sal
da3=95/100*sal
sum2=hra3+da3+sal
if(sal<=10000): 
    print("Gross Salary is", sum)
elif(sal<=20000):
    print("Gross Salary is", sum1)
elif(sal>20000):
    print("Gross salary is", sum2)
    
