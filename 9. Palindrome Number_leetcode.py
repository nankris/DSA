class Solution:
    def isPalindrome(self, x: int) -> bool:
        # If number is negative then False
        if x < 0:
            return False
        x_str = str(x)
        for i in range(len(x_str)//2):
            if x_str[i] != x_str[len(x_str)-i-1]:
                return False
        return True        

solver = Solution()

# Call the isPalindrome method
number = 121
result = solver.isPalindrome(number)
print(f"Is {number} a palindrome? {result}")

number = -121
result = solver.isPalindrome(number)
print(f"Is {number} a palindrome? {result}")