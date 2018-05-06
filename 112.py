from common import TreeNode


class Solution:
    def hasPathSum(self, root, sum):
        self.sum = sum
        return self.f(root, 0)

    def f(self, node, sum):
        if not node:
            return False
        if not node.left and not node.right:
            return sum + node.val == self.sum
        return self.f(node.left, sum + node.val) or self.f(node.right, sum + node.val)


if __name__ == '__main__':
    solution = Solution()
    print(solution.hasPathSum(TreeNode.list2Tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]),22))
