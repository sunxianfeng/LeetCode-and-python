# -*- coding:utf-8 -*-
from collections import deque
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def dfs(root, h):
            if root:
                if h == len(ans):
                    ans.append(root.val)
                dfs(root.right, h + 1)
                dfs(root.left, h + 1)
        ans = []
        dfs(root, 0)
        return ans
# class Solution:
#     def rightSideView(self, root):
#         ans = []
#         if root is None: return ans
#         queue = [root]
#         while queue:
#             size = len(queue)
#             for i in range(size):
#                 top = queue.pop(0)
#                 if i == 0: ans.append(top.val)
#                 if top.right: queue.append(top.right)
#                 if top.left: queue.append(top.left)
#         return ans