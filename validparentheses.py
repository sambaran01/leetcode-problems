class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        res = []
        brackets = {'(': ')','{' :'}' , '[':']'}
        opening = {'(', '{', '['}
        for i in s:
            if i in opening:
                res.append(i)
            else:
                if not res:
                    return False
                last = res.pop()
                if brackets[last] != i:
                    return False
        return len(res) == 0

test = Solution()
print(test.isValid("({})"))