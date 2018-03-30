class Solution:
    def largestValues(self, root):
        res = []
        if root:
            from queue import Queue
            q = Queue()
            q.put((root, 0))
            while not q.empty():
                node, floor = q.get()
                if floor >= len(res):
                    res.append(node.val)
                else:
                    res[floor] = max(res[floor], node.val)
                if node.left:
                    q.put((node.left, floor + 1))
                if node.right:
                    q.put((node.right, floor + 1))
        return res