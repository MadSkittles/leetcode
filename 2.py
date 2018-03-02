# Add Two Numbers

# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example:
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        s = ''
        this = self
        while this:
            s += str(this.val)
            this = this.next
        return '0' if len(s) == 0 else s[::-1]


def toListNone(num: int):
    result = p = None
    while num > 0:
        digit = num % 10
        num = int(num / 10)

        if result == None:
            result = ListNode(digit)
            p = result
        else:
            node = ListNode(digit)
            p.next = node
            p = node
    return result


class Solution:
    def addTwoNumbers(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        result = cur_digit_node = None
        next_digit_add = 0

        while l1 is not None or l2 is not None:
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0

            cur_digit = (val1 + val2 + next_digit_add) % 10
            next_digit_add = int((val1 + val2 + next_digit_add) / 10)

            if result is None:
                result = ListNode(cur_digit)
                cur_digit_node = result
            else:
                next_digit_node = ListNode(cur_digit)
                cur_digit_node.next = next_digit_node
                cur_digit_node = next_digit_node

            l1, l2 = l1 and l1.next, l2 and l2.next

        if next_digit_add:
            next_digit_node = ListNode(next_digit_add)
            cur_digit_node.next = next_digit_node

        return result


if __name__ == '__main__':
    print(Solution().addTwoNumbers(toListNone(5), toListNone(5)))
