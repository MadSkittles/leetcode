from common import ListNode


class Solution:
    def __init__(self, head):
        node = self.head = head
        self.length = 0
        while node:
            self.length += 1
            node = node.next

    def getRandom(self):
        if not self.head:
            return None
        from random import randint
        index = randint(0, self.length - 1)
        node = self.head
        while index:
            node = node.next
            index -= 1
        return node.val


if __name__ == '__main__':
    solution = Solution(ListNode.list2ListNode([]))
    print(solution.getRandom())
