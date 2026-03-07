n = int(input("enter the value of n"))
value = n
reverse = 0
while value > 0:
    digit = value % 10
    reverse = reverse * 10 + digit
    value = value // 10

if n == reverse:
    print(f"the given value {n} is a palindrome ")
else:
    print(f"the given value {n} is not a palindrome")

