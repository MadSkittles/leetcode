from common import TreeNode


class Solution:
    def buildTree(self, inorder, postorder):
        if not postorder or not inorder:
            return None
        return self.f(inorder, postorder)

    def f(self, inorder: list, postorder: list):
        index = inorder.index(postorder[-1])
        node = TreeNode(postorder[-1])
        if index > 0:
            node.left = self.f(inorder[:index], postorder[:index])
        if index < len(inorder) - 1:
            node.right = self.f(inorder[index + 1:], postorder[index:-1])
        return node


if __name__ == '__main__':
    solution = Solution()
    print(solution.buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3]))
