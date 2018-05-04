from common import ListNode


class Solution:
    def mergeTwoLists(self, l1, l2):
        head, p1, p2 = ListNode(None), l1, l2
        p = head
        while p1 and p2:
            min_p = min(p1, p2, key=lambda p: p.val if p else float('-inf'))
            p.next = min_p
            p = p.next
            if min_p == p1:
                p1 = p1.next
            else:
                p2 = p2.next
            min_p.next = None
        p.next = p1 or p2
        return head.next


if __name__ == '__main__':
    solution = Solution()
    print(solution.mergeTwoLists(ListNode.list2ListNode([]), ListNode.list2ListNode([])))
