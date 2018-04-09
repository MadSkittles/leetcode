from common import TreeNode


class Solution:
    def printTree(self, root):
        if not root:
            return [[]]
        from queue import Queue
        q, depth = Queue(), float('-inf')
        q.put((root, 1))
        while not q.empty():
            node, cur_depth = q.get()
            depth = max(depth, cur_depth)
            if node.left:
                q.put((node.left, cur_depth + 1))
            if node.right:
                q.put((node.right, cur_depth + 1))
        col = 0
        for _ in range(depth):
            col = 2 * col + 1
        res = [[''] * col for _ in range(depth)]
        q.put((root, 0, 0, col - 1))
        while not q.empty():
            node, depth, lo, hi = q.get()
            mid = (lo + hi) // 2
            res[depth][mid] = str(node.val)
            if node.left:
                q.put((node.left, depth + 1, lo, mid - 1))
            if node.right:
                q.put((node.right, depth + 1, mid + 1, hi))
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.printTree(TreeNode.list2Tree([1, 2, None])))
    print(solution.printTree(TreeNode.list2Tree([1, 2, 3, None, 4])))
    print(solution.printTree(TreeNode.list2Tree([1, 2, 5, 3, None, None, None, 4])))
