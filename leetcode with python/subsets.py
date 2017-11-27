# -*- coding:utf-8 -*-
def dfs(nums, start, subs, result):
    result.append(subs)
    for i in range(start, len(nums)):
        dfs(nums, i+1, subs+[nums[i]],result)
def subsets(nums):
    if nums is None: return []
    result = []
    dfs(sorted(nums), 0, [], result)
    return result
nums = [1,2,3]
re = subsets(nums)
print re