from common import ListNode


class Solution:
    def reorderList(self, head):
        if not head:
            return None
        stack = []
        p = head
        while p:
            stack.append(p)
            p = p.next
        l, p = len(stack), head
        stack = stack[l - (l // 2):]
        while len(stack):
            node = stack.pop()
            next_node = p.next
            p.next = node
            node.next = next_node
            p = next_node
        p.next = None


if __name__ == '__main__':
    solution = Solution()
    l = ListNode.list2ListNode([1, 2, 3])
    solution.reorderList(l)
    print(l)
