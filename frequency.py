nums = [1,12,21,31,42,37,21,1,19,21,29,22,9,17,21,22,29]

def frequency(nums):
    frequency_map = {}
    for i in range(0,len(nums)):
        if nums[i] in frequency_map:
            frequency_map[nums[i]] += 1
        else:
            frequency_map[nums[i]] = 1
    return frequency_map

print(frequency(nums))