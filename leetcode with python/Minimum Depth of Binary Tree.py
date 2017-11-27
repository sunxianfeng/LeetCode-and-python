# -*- coding:utf-8 -*-
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if left == right == 0:
            return 1
        if left == 0:
            return 1 + right
        if right == 0:
            return 1 + left
        return 1 + min(left, right)