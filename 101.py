from common import TreeNode


class Solution:
    def isSymmetric(self, root):
        return self.f(root, root)

    def f(self, node1, node2):
        if not node1 and not node2:
            return True
        if (not node1 and node2) or (node1 and not node2):
            return False
        return node1.val == node2.val and self.f(node1.left, node2.right) and self.f(node1.right, node2.left)


if __name__ == '__main__':
    solution = Solution()
    print(solution.isSymmetric(TreeNode.list2Tree([1, 2, 2, None, 3, None, 3])))
