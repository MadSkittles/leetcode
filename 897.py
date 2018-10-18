from common import TreeNode


class Solution:
    def increasingBST(self, root):
        res, _ = self.helper(root) if root else (root, None)
        return res

    def helper(self, node):
        left_head = left_tail = right_head = right_tail = node
        if node.left:
            left_head, left_tail = self.helper(node.left)
            left_tail.right = node
        if node.right:
            right_head, right_tail = self.helper(node.right)
            node.right = right_head
        node.left = None
        return left_head, right_tail


if __name__ == "__main__":
    solution = Solution()
    print(solution.increasingBST(TreeNode.list2Tree([5, 3, 6, 2, 4, None, 8, 1, None, None, None, 7, 9])))
