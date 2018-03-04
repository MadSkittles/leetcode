from common import TreeNode


class Solution:
    def inorderTraversal(self, root):
        return self.f(root)

    def f(self, node: TreeNode):
        if node is None:
            return []
        print(node.val)
        return self.f(node.left) + [node.val] + self.f(node.right)

if __name__ == '__main__':
    solution=Solution()
    print(solution.inorderTraversal(TreeNode.list2Tree([1,None,2,3])))