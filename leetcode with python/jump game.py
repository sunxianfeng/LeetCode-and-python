# -*- coding:utf-8 -*-
class Solution(object):
    # @param A, a list of integers
    # @return a bool
    def canJump(self, nums):
        m = len(nums)
        can = [False] * m
        can[0] = True
        for i in range(1, m):
            for j in range(0, i):
                if can[j] and nums[j] >= i - j:
                    can[i] = True
                    break
        return can[m - 1]
s = Solution()
print(s.canJump([2,3,1,1,4]))
