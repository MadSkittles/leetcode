from common import ListNode


class Solution:
    def mergeKLists(self, lists):
        head = tail = None
        while True:
            min_, index = float('inf'), -1
            for i, p in enumerate(lists):
                if p and p.val < min_:
                    index, min_ = i, p.val
            if index < 0:
                break
            min_node = lists[index]
            if head is None:
                head = tail = min_node
            else:
                tail.next = min_node
                tail = min_node
            lists[index] = min_node.next
            min_node.next = None
        return head


if __name__ == '__main__':
    solution = Solution()
    print(solution.mergeKLists([ListNode.list2ListNode([]), ListNode.list2ListNode([1, 3, 4]), ListNode.list2ListNode([2, 6])]))
