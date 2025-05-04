class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        return str(x) == str(x)[::-1]
        
test = Solution()
print(test.isPalindrome(121))
print(test.isPalindrome(-121))
print(test.isPalindrome(10))