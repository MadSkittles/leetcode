from common import TreeNode

class Solution:
    def isBalanced(self, root):
        return self.helper(root)[0] if root else True

    def helper(self, node):
        if not node.left and not node.right:
            return True, 1
        is_left_balanced, left_height = True, 0
        if node.left:
            is_left_balanced, left_height = self.helper(node.left)
        is_right_balanced, right_height = True, 0
        if is_left_balanced and node.right:
            is_right_balanced, right_height = self.helper(node.right)
        return is_left_balanced and is_right_balanced and abs(left_height - right_height) <= 1, 1 + max(left_height, right_height)


if __name__ == '__main__':
    solution = Solution()
    print(solution.isBalanced(TreeNode.list2Tree([1, None, 2, None, 3])))
