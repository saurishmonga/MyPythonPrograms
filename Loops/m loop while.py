cd=int(input("Enter a number: "))
ui=cd%10
while(cd>10):
    cd=cd//10
print(ui+cd)
