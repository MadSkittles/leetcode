class Solution:
    def rightSideView(self, root):
        self.result = []
        res = ()
        if root:
            self.f(root, (root.val,))
            for p in self.result:
                if len(p) > len(res):
                    res += p[len(res) - len(p):]
        return res

    def f(self, node, path):
        if not node.left and not node.right:
            self.result.append(path)
            return
        if node.right:
            self.f(node.right, (*path, node.right.val))
        if node.left:
            self.f(node.left, (*path, node.left.val))
