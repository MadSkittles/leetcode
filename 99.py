from common import TreeNode


class Solution:
    def recoverTree(self, root):
        if not root:
            return None
        self.data, self.index = [], 0
        self.f(root)
        self.data.sort()
        self.f(root, False)

    def f(self, node, record=True):
        if node.left:
            self.f(node.left, record)
        if record:
            self.data.append(node.val)
        else:
            node.val = self.data[self.index]
            self.index += 1
        if node.right:
            self.f(node.right, record)


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode.list2Tree([3, 1, 4, None, None, 2])
    solution.recoverTree(root)
    print(root)
    # print(solution.recoverTree(TreeNode.list2Tree([3, 1, 4, None, None, 2])))
