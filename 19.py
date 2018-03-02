from common import ListNode


class Solution:
    def removeNthFromEnd(self, head, n):
        slow_pointer, fast_pointer = head, head
        while n > 0:
            fast_pointer = fast_pointer.next
            n -= 1

        if fast_pointer is None:
            return head.next

        while fast_pointer.next is not None:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next
        slow_pointer.next = slow_pointer.next.next

        return head


if __name__ == '__main__':
    solution = Solution()
    print(solution.removeNthFromEnd(ListNode.build([1]), 1))
