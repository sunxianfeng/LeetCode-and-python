# -*- coding:utf-8 -*-
def singleNumber(nums):
    xor = 0
    for num in nums:
        xor ^= num
    xor = xor & -xor
    a, b = 0, 0
    for num in nums:
        if num & xor:
            a ^= num
        else:
            b ^= num
    return a, b
nums = [1,1,2,2,3,5]
res = singleNumber(nums)
print res