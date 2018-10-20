from common import ListNode


class Solution:
    def middleNode(self, head):
        l, p = 0, head
        while p:
            l += 1
            p = p.next
        i, p = 0, head
        while i < l // 2:
            p = p.next
            i += 1
        return p


if __name__ == "__main__":
    solution = Solution()
    print(solution.middleNode(ListNode.list2ListNode([1])))
    print(solution.middleNode(ListNode.list2ListNode([1, 2, 3, 4, 5])))
    print(solution.middleNode(ListNode.list2ListNode([1, 2, 3, 4, 5, 6])))
