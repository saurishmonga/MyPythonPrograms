phy=float(input("Enter The Marks For Physics: "))
chem=float(input("Enter The Marks For Chemistry: "))
bio=float(input("Enter The Marks For Biology: "))
maths=float(input("Enter The Marks For Mathematics: "))
com=float(input("Enter The Marks For Computers: "))
a=phy+chem+bio+maths+com
b=(a/5)
print(b)
if(b>=90):
    print(b, "GRADE: A")
elif(b>=80) and (b<90):
    print(b, "GRADE: B")
elif(b>=70) and (b<80):
    print(b, "GRADE: C")
elif(b>=60) and (b<70):
    print(b, "GRADE:D")
elif(b>=40) and (b<60):
    print(b, "GRADE: E")
elif(b<40):
    print(b, "GRADE: F")
