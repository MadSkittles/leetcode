from common import TreeNode


class Solution:
    def kthSmallest(self, root, k):
        self.k = k
        self.start = False
        return self.f(root).val

    def f(self, node):
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
    print(solution.kthSmallest(TreeNode.list2Tree([5, 3, 9, 2, 4, 7, 10, 1, None, None, None, 6, 8, None, 11]),5))
