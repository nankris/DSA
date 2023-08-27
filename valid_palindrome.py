# Using two pointer approach
def isPalindrome(s):

    left = 0
    right = len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True

s = "A man, a plan, a canal: Panama"

print(isPalindrome(s))



    ########## This is another approch, but not time and space efficient

    # new_str = ''.join(char.lower() for char in s if char.isalnum())
    # for i in range(len(new_str)):
    #     if new_str[i] == new_str[len(new_str)-i-1]:
    #         continue
    #     else:
    #         return False
    # return True
