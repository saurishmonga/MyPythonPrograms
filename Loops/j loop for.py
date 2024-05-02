num = input("Enter a number: ")
count = 0
for digit in num:
    if '0' <= digit <= '9':
        count=count+1
print(count)
