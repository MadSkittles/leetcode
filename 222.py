from common import TreeNode


class Solution:
    def countNodes(self, root):
        if not root:
            return 0
        from queue import Queue
        res, q = 0, Queue()
        q.put(root)
        while not q.empty():
            node = q.get()
            res += 1
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.countNodes(TreeNode.list2Tree([1, 2])))
