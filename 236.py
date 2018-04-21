from common import TreeNode


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if root in (None, p, q): return root
        left, right = (self.lowestCommonAncestor(kid, p, q) for kid in (root.left, root.right))
        return root if left and right else left or right

    def lowestCommonAncestorOnline(self, root, p, q):
        self.nodes, self.depth = [], []
        self.dfs(root, 0)
        p_pos, q_pos = self.nodes.index(p), self.nodes.index(q)
        min_n, min_pos = float('inf'), 0
        for i in range(min(p_pos, q_pos), max(p_pos, q_pos)):
            if self.depth[i] < min_n:
                min_n, min_pos = self.depth[i], i
        return self.nodes[min_pos]

    def dfs(self, node, depth):
        self.nodes.append(node)
        self.depth.append(depth)
        if node.left:
            self.dfs(node.left, depth + 1)
        if node.left or node.right:
            self.nodes.append(node)
            self.depth.append(depth)
        if node.right:
            self.dfs(node.right, depth + 1)


if __name__ == '__main__':
    solution = Solution()
    tree = TreeNode.list2Tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    print(solution.lowestCommonAncestorOnline(tree, tree.right.left, tree.right.right))
