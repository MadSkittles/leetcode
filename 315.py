class Solution:
    class _Node:
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None
            self.left_size = 0

    def countSmaller(self, nums):
        self.tree = None
        res = []
        for n in nums[::-1]:
            res.append(self.build_BST(self.tree, n))
        return res[::-1]

    def build_BST(self, node, n):
        if self.tree is None:
            self.tree = Solution._Node(n)
            return 0
        if n <= node.val:
            node.left_size += 1
            if node.left is None:
                node.left = Solution._Node(n)
                return 0
            else:
                return self.build_BST(node.left, n)
        else:
            if node.right is None:
                node.right = Solution._Node(n)
                return node.left_size + 1
            else:
                return node.left_size + 1 + self.build_BST(node.right, n)


if __name__ == '__main__':
    solution = Solution()
    print(solution.countSmaller([-1, -1]))
