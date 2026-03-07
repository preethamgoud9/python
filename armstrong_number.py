n = int(input("enter the value of n"))
num = n
total = 0
size = len(str(n))
while num > 0:
    digit = num % 10
    total = total + (digit ** size)
    num = num // 10

if n == total:
    print(f"the {n} is an armstrong number")
else:
    print(f"the {n} is not an armstrong number")