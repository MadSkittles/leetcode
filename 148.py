from common import ListNode

class Solution:
    def sortList(self, head):
        q = []
        p = head
        while p:
            next_node = p.next
            q.append(p)
            p.next = None
            p = next_node

        while len(q) > 1:
            next_q = []
            index = 0
            while index < len(q):
                if index + 1 < len(q):
                    next_q.append(self.merge(q[index], q[index + 1]))
                    index += 2
                else:
                    next_q.append(q[index])
                    index += 1
            q = next_q
        return q[-1] if q else None

    def merge(self, l1, l2):
        head, tail, p1, p2 = None, None, l1, l2
        while p1 and p2:
            if p1.val < p2.val:
                node = p1
                p1 = p1.next
            else:
                node = p2
                p2 = p2.next
            if head is None and tail is None:
                head = tail = node
            else:
                tail.next = node
                tail = tail.next
        if p1:
            tail.next = p1
        if p2:
            tail.next = p2
        return head

if __name__ == '__main__':
    solution = Solution()
    from random import shuffle
    l = list(range(200))
    # shuffle(l)
    print(l)
    print(solution.sortList(ListNode.list2ListNode(l)))