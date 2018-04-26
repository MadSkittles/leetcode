from common import TreeNode


class Solution:
    def findDuplicateSubtrees(self, root):
        self.pre_orders = set()
        self.res = {}
        self.f(root)
        return list(self.res.values())

    def f(self, node):
        if not node:
            return None
        pre_order = (self.f(node.left), node.val, self.f(node.right))
        if pre_order in self.pre_orders:
            self.res[pre_order] = node
        else:
            self.pre_orders.add(pre_order)
        return pre_order


if __name__ == '__main__':
    solution = Solution()
    print(solution.findDuplicateSubtrees(TreeNode.list2Tree([1, 2, 3, 4, None, 2, 4, None, None, 4])))
    print(solution.findDuplicateSubtrees(TreeNode.list2Tree([0, 0, 0, 0, None, None, 0, None, None, None, 0])))
