from common import TreeNode


class Solution:
    def preorderTraversal(self, root):
        self.res = []
        if root:
            self.f(root)
        return self.res

    def f(self, node):
        self.res.append(node.val)
        if node.left:
            self.f(node.left)
        if node.right:
            self.f(node.right)


if __name__ == '__main__':
    solution = Solution()
    print(solution.preorderTraversal(TreeNode.list2Tree([1, None, 2, 3])))
