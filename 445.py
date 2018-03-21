from common import ListNode


class Solution:
    def addTwoNumbers(self, l1, l2):
        stack1, stack2 = [], []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        next_node, add_on = None, 0
        while stack1 or stack2 or add_on:
            if stack1 and stack2:
                val = stack1.pop() + stack2.pop() + add_on
            elif stack1:
                val = stack1.pop() + add_on
            elif stack2:
                val = stack2.pop() + add_on
            else:
                val = add_on
            node = ListNode(val % 10)
            add_on = val // 10
            node.next = next_node
            next_node = node
        return next_node


if __name__ == '__main__':
    solution = Solution()
    print(solution.addTwoNumbers(ListNode.list2ListNode([0]), ListNode.list2ListNode([5, 6, 4])))
