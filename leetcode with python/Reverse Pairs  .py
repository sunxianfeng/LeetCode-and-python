# -*- coding:utf-8 -*-
# import bisect
# class Solution(object):
#     def reversePairs(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         n = len(nums)
#         ans = 0
#         bst = []
#         for num in nums:
#             right = 2 * num
#             idx = bisect.bisect_right(bst, right)
#             ans += len(bst) - idx
#             bisect.insort(bst, num)
#         return ans
class Solution:
    # @param {int[]} A an array
    # @return {int} total of reverse pairs
    def reversePairs(self, nums):
        self.tmp = [0] * len(nums)
        return self.mergeSort(nums, 0, len(nums) - 1)

    def mergeSort(self, nums, left, right):
        if left >= right: return 0

        mid = (left + right) >> 1
        ans = self.mergeSort(nums, left, mid) +\
              self.mergeSort(nums, mid + 1, right)
        i, j, k = left, mid + 1, left
        while i <= mid and j <= right:
            if nums[i] > nums[j]:
                self.tmp[k] = nums[j]
                j += 1
                ans += mid - i + 1
            else:
                self.tmp[k] = nums[i]
                i += 1
            k += 1

        while i <= mid:
            self.tmp[k] = nums[i]
            k += 1
            i += 1
        while j <= right:
            self.tmp[k] = nums[j]
            k += 1
            j += 1
        for i in range(l, right + 1):
            nums[i] = self.tmp[i]

        return ans

