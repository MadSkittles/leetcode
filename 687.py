from common import TreeNode


class Solution:
    def longestUnivaluePath(self, root):
        return max(self.dfs(root)) - 1 if root else 0

    def dfs(self, node):
        if not node.left and not node.right:
            return 1, 1
        l1, l2 = 0, 0
        if node.left:
            l1, l2 = self.dfs(node.left)
        r1, r2 = 0, 0
        if node.right:
            r1, r2 = self.dfs(node.right)
        l, r = l1 if node.left and node.val == node.left.val else 0, r1 if node.right and node.val == node.right.val else 0
        return max(l + 1, r + 1), max(l1, r1, l2, r2, l + 1 + r)


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestUnivaluePath(TreeNode.list2Tree([5, 4, 5, 1, 1, 5])))
