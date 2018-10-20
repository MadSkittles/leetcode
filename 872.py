from common import TreeNode


class Solution:
    def leafSimilar(self, root1, root2):
        return self.helper(root1) == self.helper(root2)

    def helper(self, node):
        if not node.left and not node.right:
            return (node.val,)
        return (self.helper(node.left) if node.left else ()) + (self.helper(node.right) if node.right else ())


if __name__ == "__main__":
    solution = Solution()
    print(solution.leafSimilar(TreeNode.list2Tree([18, 35, 22, None, 103, 43, 101, 58, None, 97]), TreeNode.list2Tree([94, 102, 17, 122, None, None, 54, 58, 101, 97])))
