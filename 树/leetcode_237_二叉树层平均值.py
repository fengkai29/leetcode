# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if root == None:
            return []
        res = []
        temp = [root]
        while temp:
            n = len(temp)
            count = 0
            for i in range(n):
                m = temp.pop(0)
                count += m.val
                if m.left:
                    temp.append(m.left)
                if m.right:
                    temp.append(m.right)
            res.append(count/(i+1))
        return res
