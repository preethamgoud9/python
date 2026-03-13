num = [5,7,3,2,6,1,5,9,10]

def rev(num,left,right):
    if left >= right:
        return num
    num[left],num[right] = num[right],num[left]
    return rev(num,left+1,right-1)

print(rev(num,0,len(num)-1))