from common import TreeNode


class Solution:
    def recoverTree(self, root):
        self.first, self.second, self.pre = None, None, None

        def traverse(node):
            if not node: return
            traverse(node.left)
            if self.pre and self.pre.val >= node.val:
                if not self.first:
                    self.first = self.pre
                self.second = node
            self.pre = node
            traverse(node.right)

        traverse(root)
        self.first.val, self.second.val = self.second.val, self.first.val


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode.list2Tree([3, 4, 1, 5, 2])
    solution.recoverTree(root)
    print(root)
