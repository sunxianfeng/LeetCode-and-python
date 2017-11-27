# -*- coding:utf-8 -*-
class Solution(object):
    def getHeight(self, root):
        height = 0
        while root:
            height += 1
            root = root.left
        return height

    def countNodes(self, root):
        count = 0
        while root:
            l, r = map(self.getHeight, (root.left, root.right))
            if l == r:
                count += 2 ** l
                root = root.right
            else:
                count += 2 ** r
                root = root.left
        return count

