nums = [1,12,21,31,42,37,21,1,19,21,29,22,9,17,21,22,29]

def frequency(nums):
    frequency_map = {}
    for i in range(len(nums)):
        frequency_map[nums[i]] = frequency_map.get(nums[i],0) + 1
    return frequency_map

print(frequency(nums))