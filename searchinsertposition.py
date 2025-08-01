class Solution(object):
    def searchInsert(self, nums, target):
        l = 0
        r = (len(nums) - 1)
        while l <= r:
            mid  =(l + r) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        return l
    
test = Solution()
print(test.searchInsert([1,3,5,7,9],6))