nums = [3,1,2,4,1,5,2,6,4]

def merge_array(left,right):
    n = len(left)
    m = len(right)
    result = []
    i , j = 0,0
    while i < n and j < m:
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < n:
        result.append(left[i])
        i += 1
    while j < m:
        result.append(right[j])
        j += 1
    return result

def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left_half = array[:mid]
    right_half = array[mid:]
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    return merge_array(left_half,right_half)

print(merge_sort(nums))
