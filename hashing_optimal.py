n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2]

hash_list = [0] * 11

for num in n:
    hash_list[num] += 1
print(hash_list)

for x in m:
    if x < len(hash_list):
        print(hash_list[x])
    else:
        print(0)