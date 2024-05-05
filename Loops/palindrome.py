num=int(input("Enter the value: "))
original_num = num
reverse_num = 0
while num > 0:
        remainder = num % 10
        reverse_num = reverse_num * 10 + remainder
        num = num // 10
    
if original_num == reverse_num:
    print(original_num, "is a palindrome.")
else:
    print(original_num, "is not a palindrome.")

