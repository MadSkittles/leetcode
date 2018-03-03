from common import ListNode


class Solution:
    def swapPairs(self, head: ListNode):
        if head is None or head.next is None:
            return head

        pre, post = head, head.next
        head = post
        pre_pre = None
        while post:
            post_next = post.next
            post.next = pre
            pre.next = post_next

            if pre_pre:
                pre_pre.next = post
            pre_pre = pre
            pre = post_next
            post = pre.next if pre else None

        return head


if __name__ == '__main__':
    solution = Solution()
    print(solution.swapPairs(ListNode.list2ListNode([])))
