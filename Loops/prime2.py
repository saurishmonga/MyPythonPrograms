num = int(input("Enter a number: "))
if num <= 1:
    print(num, "is not a prime number")
else:
    fact = 0
    for i in range(2, num):
        if num % i == 0:
            fact = 1
    if fact == 1:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")
