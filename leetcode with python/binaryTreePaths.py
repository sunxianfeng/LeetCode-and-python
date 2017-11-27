# -*- coding:utf-8 -*-
from collections import deque
class Solution:
    def binaryTreePaths(self, root):
        if root is None: return []
        queue = deque([root, str(root.val)])
        ans = []
        while queue:
            top, path = queue.popleft()
            if top.left is None and top.right is None:
                ans += path
                continue
            if top.left:
                queue += [top.left, path + "->" + str(top.left.val)]
            if top.right:
                queue += [top.right, path + "->" + str(top.right.val)]
        return ans

# class Solution:
#     # @param {TreeNode} root the root of the binary tree
#     # @return {List[str]} all root-to-leaf paths
#     def dfs(self, node, result, tmp):
#         tmp.append(str(node.val))
#         if node.left is None and node.right is None:
#             result.append('->'.join(tmp))
#             tmp.pop()
#             return
#         if node.left:
#             self.dfs(node.left, result, tmp)
#         if node.right:
#             self.dfs(node.right, result, tmp)
#         tmp.pop()
#
#     def binaryTreePaths(self, root):
#         result = []
#         if root is None: return result
#         self.dfs(root, result, [])
#         return result