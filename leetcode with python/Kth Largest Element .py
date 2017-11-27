# -*- coding:utf-8 -*-
class Solution:
    # @param k & A a integer and an array
    # @return ans a integer
    def partition(self, nums, left, right):
        low, high = left, right
        pivot = nums[low]
        while low < high:
            while low < high and nums[high] >= pivot:
                high -= 1
            nums[low] = nums[high]
            while low < high and nums[low] <= pivot:
                low += 1
            nums[high] = nums[low]
        nums[low] = pivot
        return low

    def helper(self, nums, left, right, k):
        if left == right: return nums[left]
        position = self.partition(nums, left, right)
        if position + 1 == k: return nums[position]
        elif position + 1 < k: return self.helper(nums, position+1, right, k)
        else: return self.helper(nums, left, position-1, k)

    def kthLargestElement(self, k, nums):
        if len(nums) == 0 or k <= 0: return 0
        return self.helper(nums, 0, len(nums) - 1, len(nums) - k + 1)


