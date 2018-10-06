from common import TreeNode


class Solution:
    def insertIntoBST(self, root, val):
        self.helper(root, val)
        return root

    def helper(self, node, val):
        if node is None:
            return TreeNode(val)
        if val > node.val:
            node.right = self.helper(node.right, val)
        else:
            node.left = self.helper(node.left, val)
        return node


if __name__ == "__main__":
    solution = Solution()
    print(solution.insertIntoBST(TreeNode.list2Tree([4, 2, 7, 1, 3]), 5))

