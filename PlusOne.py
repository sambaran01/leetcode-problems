class Solution(object):
    def plusOne(self, digits):
        n = int(''.join(map(str, digits)))
        n += 1
        return [int(d) for d in str(n)]

test=Solution()
print(test.plusOne([9]))
print(test.plusOne([9,9]))
print(test.plusOne([1,4,8,9]))
