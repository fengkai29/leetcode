"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        res = []
        que = [root]
        if root == None:
            return res
        while que:
            tempList = []
            for i in range(len(que)):
                node = que.pop(0)
                tempList.append(node.val)
                if node.children:
                    que.extend(node.children)
            res.append(tempList)
        return res



