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
    def build(cls, l: list):
        if not l:
            return None
        p = head = cls(l[0])
        for i in l[1:]:
            node = ListNode(i)
            p.next = node
            p = p.next
        return head
