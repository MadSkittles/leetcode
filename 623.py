from common import TreeNode


class Solution:
    def addOneRow(self, root, v, d):
        if d == 1:
            node = TreeNode(v)
            node.left = root
            return node
        from queue import Queue
        q = Queue()
        q.put((root, 1))
        while not q.empty():
            n, depth = q.get()
            if depth == d - 1:
                left_node, right_node = TreeNode(v), TreeNode(v)
                left_node.left, right_node.right = n.left, n.right
                n.left, n.right = left_node, right_node
            else:
                if n.left:
                    q.put((n.left, depth + 1))
                if n.right:
                    q.put((n.right, depth + 1))
        return root
