# -*- coding:utf-8 -*-
class Solution:
    def preorder(self, root, level, res):
        if root:
            if len(res) < level+1: res.append([])
            if level % 2 == 0:
                res[level].append(root.val)
            else:
                res[level].insert(0, root.val)
            self.preorder(root.left, level+1, res)
            self.preorder(root.right, level+1, res)
    def zigzagLevelOrder(self, root):
        self.results = []
        self.preorder(root, 0, self.results)
        return self.results

# from collections import deque
# class Solution(object):
#     def zigzagLevelOrder(self, root):
#         """
#         :type root: TreeNode
#         :rtype: List[List[int]]
#         """
#         stack = deque([root])
#         ans = []
#         odd = True
#         while stack:
#             level = []
#             for k in xrange(0, len(stack)):
#                 top = stack.popleft()
#                 if top is None: continue
#                 level.append(top.val)
#                 stack.append(top.left)
#                 stack.append(top.right)
#             if level:
#                 if odd: ans.append(level)
#                 else: ans.append(level[::-1])
#             odd = not odd
#         return ans