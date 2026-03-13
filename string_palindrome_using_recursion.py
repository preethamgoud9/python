s = 'markram'

def palindrome(s,left,right):
    if left >= right:
        return "it is an palindrome"
    if s[left] != s[right]:
        return "not an palindrome"
    return palindrome(s,left+1,right-1)

print(palindrome(s,0,len(s)-1))