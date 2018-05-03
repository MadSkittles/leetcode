from common import TreeNode


class Solution:
    def maxPathSum(self, root):
        return max(self.f(root))

    def f(self, node):
        if not node.left and not node.right:
            return node.val, node.val
        left1, left2 = float('-inf'), float('-inf')
        if node.left:
            left1, left2 = self.f(node.left)
        right1, right2 = float('-inf'), float('-inf')
        if node.right:
            right1, right2 = self.f(node.right)
        n = float('-inf')
        if node.left and left2 > 0 and node.right and right2 > 0:
            n = node.val + left2 + right2
        return max(n, left1, left2, right1, right2), max(node.val + left2, node.val + right2, node.val)


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxPathSum(TreeNode.list2Tree([-3])))
    print(solution.maxPathSum(TreeNode.list2Tree([-10, 9, 20, None, None, 15, 7])))
    print(solution.maxPathSum(TreeNode.list2Tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])))
