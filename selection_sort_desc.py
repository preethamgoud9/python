nums = [5,7,8,4,1,6,9,2]

for i in range(len(nums)):
    max_index = i
    for j in range(i+1,len(nums)):
        if nums[j] > nums[max_index]:
            max_index = j
    nums[i],nums[max_index] = nums[max_index],nums[i]

print(nums)