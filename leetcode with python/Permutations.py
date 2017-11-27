# -*- coding:utf-8 -*-
class Solution(object):
    def dfs(self, nums, path, res, visited):
        if len(path) == len(nums):
            res.append(path + [])
            return

        for i in range(0, len(nums)):
            # if i > 0 and nums[i - 1] == nums[i]:
            #     continue
            if i not in visited:
                visited.add(i)
                path.append(nums[i])
                self.dfs(nums, path, res, visited)
                path.pop()
                visited.discard(i)
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        visited = set([])
        self.dfs(nums, [], res, visited)
        return res
s = Solution()
print(s.permute([1,2,3]))