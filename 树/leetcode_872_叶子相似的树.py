# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversal(self, root, ls):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return
        elif root.left == None and root.right == None:
            ls.append(root.val)
        self.preorderTraversal(root.left, ls)
        self.preorderTraversal(root.right, ls)
        return ls
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        ro = []
        ro1 = Solution().preorderTraversal(root1,ro)
        ro = []
        ro2 = Solution().preorderTraversal(root2,ro)

        if ro1 == ro2:
            return True
        else:
            return False