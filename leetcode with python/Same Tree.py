# -*- coding:utf-8 -*-
def isSameTree(p, q):
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """
    if not p or not q:
        return p == q
    return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


s = Solution()
print s.generateParenthesis(1)