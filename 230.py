from common import TreeNode


class Solution:
    def kthSmallest(self, root, k):
        self.k = k
        return self.f(root, 0)[0].val

    def f(self, node, l):
        res, left_l, right_l = None, 0, 0
        if node.left:
            res, left_l = self.f(node.left, l)
        if not res and l + left_l + 1 == self.k:
            return node, None
        if not res and node.right:
            res, right_l = self.f(node.right, left_l + 1 + l)
        return (None, left_l + 1 + right_l) if not res else (res, None)

    def kthSmallest1(self, root, k):
        self.k = k
        self.start = False
        return self.f1(root).val

    def f1(self, node):
        res = None
        if node.left:
            res = self.f(node.left)
        elif not self.start:
            self.start = True
        if self.start:
            if not res and self.k == 1:
                res = node
            else:
                self.k -= 1
        if not res and node.right:
            res = self.f(node.right)
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.kthSmallest(TreeNode.list2Tree([5, 3, 9, 2, 4, 7, 10, 1, None, None, None, 6, 8, None, 11]), 11))
