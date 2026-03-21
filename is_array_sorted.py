nums = [1,2,5,8,3,10,14,15]
n = len(nums)
for i in range(0,n-1):
    if nums[i] > nums[i+1]:
        print("not sorted")
        break
else:
    print("sorted")
