# -*- coding:utf-8 -*-
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        def delete(root, pre):
            if root.right:
                p = root.right
                while p.left:
                    p = p.left
                p.left = root.left
            if root is pre.left:
                pre.left = root.right or root.left
            if root is pre.right:
                pre.right = root.right or root.left
            root.left = None

        if not root: return root
        pre = dummy = TreeNode(float("inf"))
        dummy.left = root
        p = dummy
        while p:
            if key > p.val:
                pre = p
                p = p.right
            elif key < p.val:
                pre = p
                p = p.left
            else:
                delete(p, pre)
                break
        return dummy.left
