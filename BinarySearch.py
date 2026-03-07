def binary_search(arr,target):
    start = 0
    end = len(arr) - 1
    
    while start <= end:
        mid = (start + end) //2

        if target > arr[mid]:
            start = mid + 1
        elif target < arr[mid]:
            end = mid - 1
        else:
            return mid
        
    
    return -1

arr = [1,3,5,7,9,11,13,15]
result = binary_search(arr,11)
print(result)