from common import ListNode


class Solution:
    def reverseBetween(self, head, m, n):
        p = head
        index = 1
        while p and index < m - 1:
            p = p.next
            index += 1
        if p == head and m <= 1:
            pre_start = None
            p = head
        else:
            pre_start = p
            p = p.next
            index += 1

        pre_p, p, index = p, p.next, index + 1
        while p and index <= n:
            next_p = p.next
            p.next = pre_p
            pre_p = p
            p = next_p
            index += 1

        if pre_start is None:
            head.next = p
            head = pre_p
        else:
            pre_start.next.next = p
            pre_start.next = pre_p

        return head


if __name__ == '__main__':
    solution = Solution()
    print(solution.reverseBetween(ListNode.list2ListNode([1]), 1, 1))
