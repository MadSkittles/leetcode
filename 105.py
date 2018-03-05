from common import TreeNode


class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        return self.f(preorder, inorder)

    def f(self, preorder: list, inorder: list):
        index = inorder.index(preorder[0])
        node = TreeNode(preorder[0])
        if index > 0:
            node.left = self.f(preorder[1:1 + index], inorder[:index])
        if index < len(inorder) - 1:
            node.right = self.f(preorder[index + 1:], inorder[index + 1:])
        return node


if __name__ == '__main__':
    solution = Solution()
    print(solution.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]))
