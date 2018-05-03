from common import TreeNode


class Codec:
    def serialize(self, root):
        if not root:
            return ''
        res = []
        from queue import Queue
        q = Queue()
        q.put(root)
        while not q.empty():
            node = q.get()
            res.append(str(node.val) if node else '#')
            if node:
                q.put(node.left)
                q.put(node.right)
        while res and res[-1] == '#':
            res.pop()
        return ' '.join(res)

    def deserialize(self, data):
        if not data:
            return None
        nodes, index = data.split(' '), 1
        root = TreeNode(int(nodes[0]))
        from queue import Queue
        q = Queue()
        q.put(root)
        while not q.empty() and index < len(nodes):
            node = q.get()
            if node is None:
                continue
            if index < len(nodes):
                left_node = TreeNode(int(nodes[index])) if nodes[index] != '#' else None
                node.left = left_node
                q.put(left_node)
            if index + 1 < len(nodes):
                right_node = TreeNode(int(nodes[index + 1])) if nodes[index + 1] != '#' else None
                node.right = right_node
                q.put(right_node)
            index += 2
        return root


if __name__ == '__main__':
    codec = Codec()
    print(codec.deserialize(codec.serialize(TreeNode.list2Tree([5, 2, 3, None, None, 2, 4, 3, 1]))))
