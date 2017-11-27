# -*- coding:utf-8 -*-
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        cntDict, res = {}, []
        for i in nums:
            cntDict[i] = cntDict[i] + 1 if i in cntDict else 1
        bucket = [[] for i in range(len(nums)+1)]
        for key in cntDict:
            bucket[cntDict[key]].append(key)
        for i in range(len(bucket)-1, -1, -1):
            if bucket[i]:
                res.extend(bucket[i])
            if len(res) >= k:
                break
        return res[:k]
s = Solution()
print(s.topKFrequent([1,1,1,2,2,3], 2))