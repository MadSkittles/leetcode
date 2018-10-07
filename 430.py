class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

    def __setattr__(self, name, value):
        if name == "next" and value:
            value.prev = self
        super().__setattr__(name, value)


class Solution(object):
    def flatten(self, head):
        stack = []
        res = p = head
        while p or stack:
            if not p.next and stack:
                p.next = stack.pop()
                p.next.prev = p
            if p.child:
                if p.next:
                    stack.append(p.next)
                p.next = p.child
                p.next.prev = p
                p.child = None
            p = p.next
        return res


if __name__ == "__main__":
    solution = Solution()

    nodes = {i: Node(i, None, None, None) for i in range(1, 13)}
    nodes[1].next = nodes[2]
    nodes[2].next = nodes[3]
    nodes[3].next = nodes[4]
    nodes[4].next = nodes[5]
    nodes[5].next = nodes[6]
    nodes[7].next = nodes[8]
    nodes[8].next = nodes[9]
    nodes[9].next = nodes[10]
    nodes[11].next = nodes[12]
    nodes[3].child = nodes[7]
    nodes[8].child = nodes[11]
    solution.flatten(nodes[1])
    print(1)
