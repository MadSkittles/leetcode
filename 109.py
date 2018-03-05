from common import ListNode, TreeNode


class Solution:
    def sortedListToBST(self, head):
        p = head
        l = []
        while p:
            l.append(p.val)
            p = p.next
        return self.f(l) if head else []

    def f(self, l: list):
        mid = (len(l) - 1) // 2
        node = TreeNode(l[mid])
        if mid > 0:
            node.left = self.f(l[:mid])
        if mid < len(l) - 1:
            node.right = self.f(l[mid + 1:])
        return node


if __name__ == '__main__':
    solution = Solution()
    print(solution.sortedListToBST(ListNode.list2ListNode([])))
