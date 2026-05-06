def floor(nums,target):
    left = 0
    right = len(nums) - 1

    if target < nums[0]:
        return -1

    while left <= right:
        mid = (right + left) // 2

        if target == nums[mid]:
            return nums[mid]
        
        elif target < nums[mid]:
            right = mid - 1
        
        elif target > nums[mid]:
            left = mid + 1
    
    return nums[right]

nums = [2,3,5,9,14,16,18]

print(floor(nums,15))
        
