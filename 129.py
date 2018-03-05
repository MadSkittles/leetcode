from common import TreeNode


class Solution:
    def sumNumbers(self, root):
        self.result = 0
        if root:
            self.f(root, root.val)
        return self.result

    def f(self, node, num):
        if node.left is None and node.right is None:
            self.result += num
            return
        if node.left:
            self.f(node.left, num * 10 + node.left.val)
        if node.right:
            self.f(node.right, num * 10 + node.right.val)


if __name__ == '__main__':
    solution = Solution()
    print(solution.sumNumbers(TreeNode.list2Tree([1, None, 3])))
