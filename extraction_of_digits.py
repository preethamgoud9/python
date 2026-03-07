n = int(input("enter the value of n"))
num = n
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

if n == rev:
    print("it is palindrome")
else:
    print("it is not an palindrome")
