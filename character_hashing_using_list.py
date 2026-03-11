s = "azyxyyzaaaa"
q = ['d','a','y','x']

hash_list = [0] * 26

for char in s:
    asci_val = ord(char)
    index = asci_val - 97
    hash_list[index] += 1

for char in q:
    asci_val = ord(char)
    index = asci_val - 97
    print(hash_list[index])