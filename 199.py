class Solution:
    def rightSideView(self, root):
        if not root:
            return []
        from queue import Queue

        q, m = Queue(), {}
        q.put((root, 0))
        while not q.empty():
            node, floor = q.get()
            m[floor] = node.val
            if node.left:
                q.put((node.left, floor + 1))
            if node.right:
                q.put((node.right, floor + 1))
        return [m[i] for i in range(len(m))]

    def rightSideView1(self, root):
        self.result = []
        res = ()
        if root:
            self.f(root, (root.val,))
            for p in self.result:
                if len(p) > len(res):
                    res += p[len(res) - len(p) :]
        return res

    def f(self, node, path):
        if not node.left and not node.right:
            self.result.append(path)
            return
        if node.right:
            self.f(node.right, (*path, node.right.val))
        if node.left:
            self.f(node.left, (*path, node.left.val))
