# -*- coding:utf-8 -*-
def dfs(root, res, tmp=list()):
    if root is None:
        return
    tmp.append(root)
    # 这里需要用拷贝而不是用 = 赋值，也可以遍历赋值
    tmp1 = copy.deepcopy(tmp)

    if root.lchild is None and root.rchild is None:
        res.append([i.item for i in tmp])
        return

    if root.lchild is not None:
        dfs(root.lchild, res, tmp)

    # 遍历右子树需要带上不同的变量，否则左子树的tmp和右子树的tmp都指向一块内存
    if root.rchild is not None:
        dfs(root.rchild, res, tmp1)