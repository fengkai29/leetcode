# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.ls = []
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        self.ls.append(root.val)
        if root.left != None:
            self.isUnivalTree(root.left)
        if root.right != None:
            self.isUnivalTree(root.right)
        if self.ls.count(self.ls[0]) == len(self.ls):
            return True
        else:
            return False