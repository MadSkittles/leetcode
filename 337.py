from common import TreeNode


class Solution:
    def rob(self, root):
        if not root:
            return 0
        return max(self.f(root))

    def f(self, node):
        if not node.left and not node.right:
            return (0, node.val)
        left = self.f(node.left) if node.left else (0, 0)
        right = self.f(node.right) if node.right else (0, 0)
        return max([left[i] + right[j] for i in (0, 1) for j in (0, 1)]), node.val + left[0] + right[0]


if __name__ == '__main__':
    solution = Solution()
    print(solution.rob(TreeNode.list2Tree([3, 2, 3, None, 3, None, 1])))
    print(solution.rob(TreeNode.list2Tree([3, 4, 5, 1, 3, None, 1])))
