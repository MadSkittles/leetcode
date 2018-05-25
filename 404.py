from common import TreeNode


class Solution:
    def sumOfLeftLeaves(self, root):
        if not root:
            return 0
        return self.dfs(root)

    def dfs(self, node, is_left=False):
        if node.left is None and node.right is None and is_left:
            return node.val
        return (self.dfs(node.left, True) if node.left else 0) + (self.dfs(node.right) if node.right else 0)


if __name__ == '__main__':
    solution = Solution()
    print(solution.sumOfLeftLeaves(TreeNode.list2Tree([3, 9, 20, None, None, 15, 7])))
