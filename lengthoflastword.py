class Solution(object):
    def lengthOfLastWord(self, s):
        s = s.rstrip()
        c = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] != " ":
                c += 1
            else:
                return c
        return c
            
test = Solution()
print(test.lengthOfLastWord("e"))