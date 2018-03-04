from common import TreeNode


class Solution:
    def pathSum(self, root, sum):
        if not root:
            return []
        self.sum = sum
        self.res = []
        self.f(root, root.val, (root.val,))
        return self.res

    def f(self, node, cur_sum, path):
        if cur_sum == self.sum and not node.left and not node.right:
            self.res.append(path)
            return

        if node.left:
            self.f(node.left, cur_sum + node.left.val, (*path, node.left.val))
        if node.right:
            self.f(node.right, cur_sum + node.right.val, (*path, node.right.val))


if __name__ == '__main__':
    solution = Solution()
    print(solution.pathSum(TreeNode.list2Tree([-2,None,-3]), -5))
