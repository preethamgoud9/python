def ceiling(nums,target):
	left = 0
	right = len(nums) - 1
	
	if target > nums[-1]:
		return -1

	while left <= right:
		mid = (right + left) // 2
		if target == nums[mid]:
			return mid
		elif target < nums[mid]:
			right = mid - 1
		elif target > nums[mid]:
			left = mid + 1
	return nums[left]

nums = [2,3,5,9,14,16,18]
print(ceiling(nums,15))
