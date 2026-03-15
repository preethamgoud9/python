string = 'markram'

def palindrome(string,left,right):
    if left >= right:
        return "it is an palindrome"
    if string[left] != string[right]:
        return "not an palindrome"
    return palindrome(string,left+1,right-1)

result = palindrome(string,0,len(string)-1)
print(result)