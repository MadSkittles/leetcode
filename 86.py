from common import ListNode


class Solution:
    def partition(self, head: ListNode, x):
        if head is None:
            return None
        p = head
        while p.next and p.val < x and p.next.val < x:
            p = p.next

        left_tail = p if head.val < x else None
        pre_p = p
        p = p.next
        while p:
            if p.val < x:
                pre_p.next = p.next
                if left_tail is None:
                    p.next = head
                    head = p
                else:
                    p.next = left_tail.next
                    left_tail.next = p
                left_tail = p
                p = pre_p.next
            else:
                pre_p = p
                p = p.next

        return head


if __name__ == '__main__':
    solution = Solution()
    print(solution.partition(ListNode.list2ListNode([2, 1]), 2))
