for num in range(1,1001):
    original = num
    size = len(str(num))
    result = 0
    temp = num
    for i in range(size):
        digit = temp % 10
        result += (digit ** size)
        temp = temp // 10
    if original == result:
        print(original)


