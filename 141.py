from common import ListNode


class Solution(object):
    def hasCycle(self, head):
        if not head:
            return False
        p1, p2 = head, head.next.next if head.next else None
        while p1 and p2 and p2.next and p1 != p2:
            p1, p2 = p1.next, p2.next.next
        return p1 == p2 != None


if __name__ == '__main__':
    solution = Solution()
    l = ListNode.list2ListNode([3, 2, 0, -4])
    l.next.next.next.next = l.next
    print(solution.hasCycle(l))
