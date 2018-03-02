from common import ListNode


class Solution:
    def rotateRight(self, head: ListNode, k):
        if head is None:
            return None
        p = head
        l = 1
        while p.next is not None:
            l += 1
            p = p.next
        tail = p
        p = head
        k = (l - k) % l
        if k > 0:
            for i in range(1, k):
                p = p.next
            tail.next = head
            head = p.next
            p.next = None

        return head


if __name__ == '__main__':
    solution = Solution()
    print(solution.rotateRight(ListNode.build([1, 2, 3, 4, 5]), 1))
