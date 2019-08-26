# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        a = []
        self.vice(self,root,a)
        return a
    def vice(self,root,a):
        if root != None:
            self.vice(root.left,a)
            a.append(root.val)
            self.vice(root.right,a)
