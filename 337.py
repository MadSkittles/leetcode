class Solution:
    def rob(self, root):
        if not root:
            return 0
        return max(self.f(root))

    def f(self, node):
        if not node.left and not node.right:
            return (0, node.val)
        left = self.f(node.left) if node.left else (0, 0)
        right = self.f(node.right) if node.right else (0, 0)
        return max([left[i] + right[j] for i in (0, 1) for j in (0, 1)]), node.val + left[0] + right[0]