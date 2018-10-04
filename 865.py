from common import TreeNode


class Solution:
    def subtreeWithAllDeepest(self, root):
        node, _ = self.helper(root, 1)
        return node

    def helper(self, node, depth):
        if not node:
            return None, float("-inf")
        if not node.left and not node.right:
            return node, depth
        left, left_depth = self.helper(node.left, depth + 1)
        right, right_depth = self.helper(node.right, depth + 1)
        if right_depth > left_depth:
            return right, right_depth
        elif left_depth > right_depth:
            return left, left_depth
        else:
            return node, left_depth


if __name__ == "__main__":
    solution = Solution()
    print(solution.subtreeWithAllDeepest(TreeNode.list2Tree([0, 1, 3, None, 2])))

