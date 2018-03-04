from queue import Queue


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        res = []
        p = self
        while p:
            res.append(p.val)
            p = p.next
        return str(res)

    __repr__ = __str__

    @classmethod
    def list2ListNode(cls, l: list):
        if not l:
            return None
        p = head = cls(l[0])
        for i in l[1:]:
            node = ListNode(i)
            p.next = node
            p = p.next
        return head


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return '({left} <- {val} -> {right})'.format(left=self.left, val=self.val, right=self.right)

    __repr__ = __str__

    @classmethod
    def list2Tree(cls, l: list):
        nodes = []
        for i in l:
            nodes.append(TreeNode(i) if i else None)

        if not nodes:
            return nodes

        q = Queue()
        q.put(nodes[0])
        index = 1
        while index < len(nodes):
            next_floor = []
            while not q.empty():
                node = q.get()
                if node:
                    if index < len(nodes):
                        node.left = nodes[index]
                        next_floor.append(nodes[index])
                        index += 1
                    if index < len(nodes):
                        node.right = nodes[index]
                        next_floor.append(nodes[index])
                        index += 1
            for node in next_floor:
                q.put(node)

        return nodes[0] if len(nodes) else None
