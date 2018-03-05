from common import TreeNode


class Solution:
    def flatten(self, root):
        if not root:
            return
        self.f(root)

    def f(self, node):
        tail, left_subtree, right_subtree = node, node.left, node.right
        if left_subtree:
            left_subtree = self.f(left_subtree)
            tail.right = left_subtree
            while tail.right:
                tail = tail.right
        if right_subtree:
            right_subtree = self.f(right_subtree)
            tail.right = right_subtree
        node.left = None
        return node


if __name__ == '__main__':
    solution = Solution()
    tree = TreeNode.list2Tree([1, 2, 5, 3, 4, None, 6])
    solution.f(tree)
    print(tree)
