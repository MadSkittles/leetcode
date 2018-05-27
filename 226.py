from common import TreeNode


class Solution:
    def invertTree(self, root):
        if not root:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root


if __name__ == '__main__':
    solution = Solution()
    print(solution.invertTree(TreeNode.list2Tree([4, 2, 7, 1, 3, 6, 9])))
