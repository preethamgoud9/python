num = [5,7,3,2,6,1,5,9,10]

def rev(num):
    left = 0
    right = len(num) - 1
    while left < right:
        num[left],num[right] = num[right],num[left]
        left += 1
        right -= 1
    print(num)

rev(num)