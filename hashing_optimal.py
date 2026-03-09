n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2]

hash_list = [0] * 11

for num in n:
    hash_list[num] += 1
print(hash_list)

for x in m:
    if x < 0 or x >= len(hash_list) :
        print(0)
    else:
        print(hash_list[x])