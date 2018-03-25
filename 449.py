from common import TreeNode


class Codec:
    def serialize(self, root):
        from queue import Queue
        q, res = Queue(), []
        if root:
            q.put(root)
            res.append(root.val)
            while not q.empty():
                node = q.get()
                if node.left:
                    q.put(node.left)
                    res.append(node.left.val)
                else:
                    res.append('')
                if node.right:
                    q.put(node.right)
                    res.append(node.right.val)
                else:
                    res.append('')
        return '\n'.join(map(str, res))

    def deserialize(self, data):
        from queue import Queue
        vals = data.split('\n')
        root = None
        if data:
            root = TreeNode(int(vals[0]))
            index = 1
            q = Queue()
            q.put(root)
            while index < len(vals):
                node = q.get()
                if vals[index]:
                    node.left = TreeNode(int(vals[index]))
                    q.put(node.left)
                if vals[index + 1]:
                    node.right = TreeNode(int(vals[index + 1]))
                    q.put(node.right)
                index += 2
        return root
