from common import TreeNode


class Solution:
    def pruneTree(self, root):
        if not self.f(root):
            return None
        return root

    def f(self, node):
        if node is None:
            return False
        left, right = self.f(node.left), self.f(node.right)
        if not left:
            node.left = None
        if not right:
            node.right = None
        return node.val == 1 or left or right


if __name__ == '__main__':
    solution = Solution()
    print(solution.pruneTree(TreeNode.list2Tree([1, 1, 0, 1, 1, 0, 1, 0])))
