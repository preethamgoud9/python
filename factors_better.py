n = int(input("enter the value of n"))
result = []
for i in range(1,n//2+1):
    if n%i == 0:
        result.append(i)
result.append(n)
print(result)