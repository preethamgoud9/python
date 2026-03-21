nums = [55,32,-97,99,3,67]

largest = float("-inf")

for i in nums:
    if i > largest:
        largest = i
print(largest)