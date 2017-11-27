# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # @return a list of tree node
    def creatTree(self,start,end):
        if start>end:
            return [None]
        solution=[]
        for rootval in range(start,end+1):
            left=self.creatTree(start,rootval-1)
            right=self.creatTree(rootval+1,end)
            for i in left:
                for j in right:
                    root=TreeNode(rootval)
                    root.left=i
                    root.right=j
                    solution.append(root)
        return solution
    def generateTrees(self, n):
        return self.creatTree(1,n)
s = Solution()
res = s.generateTrees(3)
