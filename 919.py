from common import TreeNode


class CBTInserter:
    def __init__(self, root):
        self.root = root
        self.l = []
        if root:
            f = [root]
            while f:
                self.l.extend(f)
                tmp_f = []
                for node in f:
                    if node.left:
                        tmp_f.append(node.left)
                    if node.right:
                        tmp_f.append(node.right)
                f = tmp_f

    def insert(self, v):
        n = len(self.l)
        self.l.append(TreeNode(v))
        if self.root:
            parent = self.l[(n - 1) // 2]
            if n & 1:
                parent.left = self.l[-1]
            else:
                parent.right = self.l[-1]
            return parent.val
        else:
            self.root = self.l[-1]
            return None

    def get_root(self):
        return self.root


if __name__ == "__main__":
    cbtInserter = CBTInserter(TreeNode.list2Tree([1, 2, 3, 4, 5, 6]))
    print(cbtInserter.insert(7))
    print(cbtInserter.insert(8))
    print(cbtInserter.get_root())
