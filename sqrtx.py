class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x
        
        l = 0
        r = x //2
        while l <= r:
            mid  = (l + r) // 2
            if mid * mid  == x:
                return mid
            elif mid * mid < x:
                l = mid + 1
            else:
                r = mid - 1
        return r

test = Solution()
print(test.mySqrt(50))