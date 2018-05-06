from common import TreeNode


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return None
        if p is root or q is root or p.val < root.val < q.val or q.val < root.val < p.val:
            return root
        if max(p.val, q.val) < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if min(p.val, q.val) > root.val:
            return self.lowestCommonAncestor(root.right, p, q)


if __name__ == '__main__':
    solution = Solution()
    tree = TreeNode.list2Tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    print(solution.lowestCommonAncestor(tree, tree.right, tree.left.right.left).val)
