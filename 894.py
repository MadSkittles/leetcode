from itertools import product

from common import TreeNode


class Solution:
    def allPossibleFBT(self, N):
        if N == 1:
            return [TreeNode(0)]
        res = []
        for i in range(1, N, 2):
            for left_root, right_root in product(self.allPossibleFBT(i), self.allPossibleFBT(N - 1 - i)):
                root = TreeNode(0)
                root.left, root.right = left_root, right_root
                res.append(root)
        return res


if __name__ == "__main__":
    solution = Solution()
    res = solution.allPossibleFBT(7)
    print(res)
