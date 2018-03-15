from common import ListNode


class Solution:
    def oddEvenList(self, head):
        if not head:
            return None
        odd, even, even_head = head, head.next, head.next
        if not even:
            return head
        while odd.next and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            odd, even = odd.next, even.next
        odd.next = even_head
        return head


if __name__ == '__main__':
    solution = Solution()
    print(solution.oddEvenList(ListNode.list2ListNode([])))
    print(solution.oddEvenList(ListNode.list2ListNode([1])))
    print(solution.oddEvenList(ListNode.list2ListNode([1, 2])))
    print(solution.oddEvenList(ListNode.list2ListNode([1, 2, 3])))
    print(solution.oddEvenList(ListNode.list2ListNode([1, 2, 3, 4])))
    print(solution.oddEvenList(ListNode.list2ListNode([1, 2, 3, 4, 5])))
