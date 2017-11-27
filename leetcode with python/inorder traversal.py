# -*- coding:utf-8 -*-
def inorderTraversal(root):
    stack = []
    res = []
    cur = root
    while cur != None or stack:
        while cur != None: #如果结点存在，则入栈，然后判断左孩子
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()  #往左走到尽头，就是pop栈顶了
        res.append(cur.val)
        cur = cur.right

    return res
