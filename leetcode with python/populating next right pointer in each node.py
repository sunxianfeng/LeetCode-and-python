class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

    def connect(self, root):
        if root and root.left and root.right:
            root.left.next = root.right
            root.right.next = root.next and root.next.left
        return self.connect(root.left) or self.connect(root.right)


'''
class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if root and root.left:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
            else:
                root.right.next = None
            self.connect(root.left)
            self.connect(root.right)
'''

