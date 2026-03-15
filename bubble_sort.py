nums = [5,8,1,6,9,2,4]

for i in range(len(nums)):
    is_swap = False
    for j in range(0,len(nums)- i - 1 ):
        if nums[j] > nums[j+1]:
            nums[j],nums[j+1] = nums[j+1],nums[j]
            is_swap = True
    if is_swap == False:
        break

print(nums)