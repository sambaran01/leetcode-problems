class Solution(object):
    def strStr(self, haystack, needle):
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1


test=Solution()
print(test.strStr("sadbutsad",'sad'))
print(test.strStr("leetcode",'leeto'))
print(test.strStr("hello",'ll'))