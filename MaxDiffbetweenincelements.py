class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_so_far = nums[0]
        max_diff = -1

        for i in range(1, len(nums)):
            if nums[i] > min_so_far:
                diff = nums[i] - min_so_far
                max_diff = max(max_diff, diff)
            else:
                min_so_far = nums[i]

        return max_diff
    
test = Solution()
print(test.maximumDifference([7,1,6,4]))        