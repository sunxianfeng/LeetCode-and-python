# -*- coding:utf-8 -*-
class Solution(object):
    def maxPathSum(self, root):
        self.ans = None
        def search(root):
            if root is None: return 0
            leftMax = search(root.left)
            rightMax = search(root.right)
            self.ans = max(max(leftMax, 0) + max(rightMax, 0) + root.val, self.ans)
            return max(leftMax, rightMax, 0) + root.val
        search(root)
        return self.ans