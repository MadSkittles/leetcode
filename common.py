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
            nodes.append(cls(i) or None)

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
            if not next_floor:
                break
            for node in next_floor:
                q.put(node)

        return nodes[0] if len(nodes) else None


class TreeLinkNode(TreeNode):
    def __init__(self, x):
        super(TreeLinkNode, self).__init__(x)
        self.next = None

    def __str__(self):
        return '({left} <- {val}, {next} -> {right})'.format(left=self.left, val=self.val,
                                                             next=self.next.val if self.next else None,
                                                             right=self.right)

    __repr__ = __str__


class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class NestedInteger:
    def __init__(self, value=None):
        self.val = value or []

    def isInteger(self):
        return type(self.val) is int

    def add(self, elem):
        if self.isInteger():
            self.val = []
        self.val.append(elem)

    def setInteger(self, value):
        self.val = value

    def getInteger(self):
        return self.val if self.isInteger() else None

    def getList(self):
        return self.val if not self.isInteger() else None

    def __repr__(self):
        if self.isInteger():
            return str(self.val)
        else:
            return '[' + ', '.join(map(lambda x: repr(x), self.val)) + ']'

    __str__ = __repr__
