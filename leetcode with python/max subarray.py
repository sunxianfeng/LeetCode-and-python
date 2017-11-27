# -*- coding:utf-8 -*-
class Solution(object):
    def maxSubArray(self, nums):
        if nums is None or len(nums) == 0:
            return 0
        maxSum = nums[0]
        minSum = 0
        sum = 0
        for num in nums:
            sum += num
            if sum - minSum > maxSum:
                maxSum = sum - minSum
            if sum < minSum:
                minSum = sum
        return maxSum


s = Solution()
print(s.maxSubarray([1,2,0,-2,-3,6,2,-1]))
# class Solution(object):
#     def maxSubArray(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         if len(nums) == 0:
#             return 0
#         preSum = maxSum = nums[0]
#         for i in xrange(1, len(nums)):
#             preSum = max(preSum + nums[i], nums[i])
#             maxSum = max(maxSum, preSum)
#         return maxSum