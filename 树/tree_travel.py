class TreeNode(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinaryTree(object):
    def __init__(self, data_list):
        self.it = iter(data_list)
        self.root = TreeNode()
        self.create_tree()

    def inorder_create(self, bt=None):
        try:
            data = next(self.it)
            if data == '#': bt = None
            else:
                bt = TreeNode(data)
                bt.left = self.inorder_create(bt.left)
                bt.right = self.inorder_create(bt.right)
        except Exception as e:
            print(e)
        return bt

    def create_tree(self):
        self.root = self.inorder_create()
        print('binary tree is succussfully created!')

    def preorder(self, bt: TreeNode):
        if bt:
            self.preorder(bt.left)
            print(bt.data, end=' ')
            self.preorder(bt.right)

    def inorder(self, bt: TreeNode):
        if bt:
            print(bt.data, end=' ')
            self.inorder(bt.left)
            self.inorder(bt.right)

    def postorder(self, bt: TreeNode):
        if bt:
            self.postorder(bt.left)
            self.postorder(bt.right)
            print(bt.data, end=' ')

    def leverl_order(self, bt: TreeNode):
        q = []
        q.append(bt)
        while len(q):
            tmp = q.pop(0)
            print(tmp.data, end=' ')
            if tmp.left:
                q.append(tmp.left)
            if tmp.right:
                q.append(tmp.right)

if __name__ == '__main__':
    s = '123##4##56##78##9##'
    bt = BinaryTree(s)
    a = TreeNode()
    print(bt.leverl_order(bt.root))
