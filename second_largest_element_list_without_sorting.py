nums = [55,32,97,-55,45,32,88,21]

largest = float('-inf')
second_largest = float("-inf")

for i in nums:
    if i > largest:
        second_largest = largest
        largest = i
    elif i > second_largest and i != largest:
        second_largest = i
    
if second_largest == float("-inf"):
    print("no second largest")
else:
    print(second_largest)
