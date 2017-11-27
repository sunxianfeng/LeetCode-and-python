# -*- coding:utf-8 -*-
def searchInsert(nums, target):
    l = 0
    r = len(nums) - 1
    pos = 0
    while l <= r:
        mid = (l + r) >> 1
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            l = mid + 1
            pos = mid + 1
        else:
            r = mid - 1
            pos = mid
    return pos