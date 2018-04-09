from common import TreeNode


class Solution:
    def widthOfBinaryTree(self, root):
        if not root:
            return 0
        from queue import Queue
        q, width = Queue(), {1: [1, 1]}
        q.put((root, 1, 1))
        while not q.empty():
            node, depth, index = q.get()
            start, end = width.get(depth + 1, [float('inf'), float('-inf')])
            if not node.left and not node.right:
                continue
            if node.left:
                start = min(start, 2 * index)
                end = max(end, 2 * index)
                q.put((node.left, depth + 1, 2 * index))
            if node.right:
                start = min(start, 2 * index + 1)
                end = max(end, 2 * index + 1)
                q.put((node.right, depth + 1, 2 * index + 1))
            width[depth + 1] = [start, end]
        return max([end - start + 1 for start, end in width.values()], default=0)


if __name__ == '__main__':
    solution = Solution()
    print(solution.widthOfBinaryTree(TreeNode.list2Tree([1, 3, 2, 5, 3, None, 9])))
    print(solution.widthOfBinaryTree(TreeNode.list2Tree([1, 3, None, 5, 3])))
    print(solution.widthOfBinaryTree(TreeNode.list2Tree([1, 3, 2, 5, None])))
    print(solution.widthOfBinaryTree(TreeNode.list2Tree([1, 3, 2, 5, None, None, 9, 6, None, None, 7])))
    print(solution.widthOfBinaryTree(TreeNode.list2Tree(
        [1, 5, 8, 9, 7, 7, 8, 1, 4, 8, 1, 9, 0, 8, 7, 1, 7, 4, 2, 9, 8, 2, 4, None, None, 9, None, None, None, 6, 0, 9, 4, 1, 0, 1, 8, 9, 0, 1, 8, 9, 1, 0, 9, 6, 2, 5, None, 2, 3, 0, 2, 4, 8, 8, 8, 5,
         0, 0, 9, 4, 9, 1, None, 0, 7, 2, 2, 3, None, 6, 1, 0, 8, 9, 9, 9, 4, 8, 4, 3, 4, 4, 0, None, None, 8, 3, 8, None, None, 0, None, 0, 4, 9, 1, 2, None, 4, 4, 0, 4, 3, 5, 5, 7, 4, 1, 6, None, 1,
         0, None, None, None, 2, 8, 7, 7, None, None, 0, 2, 5, 5, 9, 3, 3, None, 7, 6, 6, 7, 9, 8, 1, 7, 7, 7, 2, 6, None, 7, None, 4, 6, 4, 6, None, None, 9, 1, None, None, None, 5, 5, 5, 4, 2, 2, 8,
         5, 1, 1, 3, 1, 3, 7, None, 2, None, 9, 1, 4, 4, 7, 7, None, 1, 5, 6, 2, 7, 3, None, 9, 1, None, 2, 4, 4, 8, None, None, 7, None, 6, None, 7, 4, 3, 5, 8, 4, 8, 5, None, None, 8, None, None,
         None, 4, 4, None, None, None, None, 8, 3, 5, 5, None, None, None, 1, 2, 0, None, None, 9, 3, None, 8, 3, 7, 1, 8, 9, 0, 1, 8, 2, None, 4, None, None, 8, None, None, None, None, 2, None, 4, 8,
         5, 5, 3, 1, None, None, 6, None, 1, None, None, 6, None, None, None, None, 7, 3, None, None, None, 8, 6, 4, None, 6, 9, 0, 7, 8, None, None, 0, 6, 7, None, None, 0, 0, 7, 2, 3, 2, None, 0, 2,
         3, None, 0, 1, 7, 9, 0, 7, None, None, None, None, 5, 8, 2, 6, 3, 2, 0, 4, None, None, 0, 9, 1, 1, 1, None, 1, 3, None, 7, 9, 1, 3, 3, 8, None, None, None, None, 6, None, None, None, None, 9,
         8, 1, 3, 8, 3, 0, 6, None, None, 8, 5, 6, 5, 2, 1, None, 5, None, 7, 0, 0, None, 9, 3, 9, None, 3, 0, 0, 9, 1, 7, 0, 2, None, 6, 8, 5, None, None, None, None, None, 7, None, 2, 5, None, None,
         9, None, None, None, None, None, None, None, None, None, None, None, 4, 1, None, 3, 6, 6, 2, 5, 5, 9, None, None, 7, 8, None, None, 2, 7, 3, 7, 2, 5, None, 1, 3, 4, None, None, 8, 3, 6, 9,
         None, 1, None, None, None, None, 9, 7, 5, 2, None, 5, None, 6, 4, 5, None, 1, 2, 0, 6, None, 1, 6, None, None, 5, None, 7, 8, 4, 7, 8, 6, 4, None, 5, 6, 7, 9, 1, 0, 4, None, None, None, 6, 4,
         8, 4, 5, None, 0, 4, 4, 0, 1, 7, 1, None, 1, None, 3, 6, None, None, None, None, 8, None, 5, 0, 7, 5, None, None, 5, 8, None, None, 3, None, None, 8, None, 2, 4, None, None, None, None, None,
         None, None, 9, None, 9, None, 9, None, None, None, None, 7, 1, None, None, 2, None, None, 5, 5, 5, 5, 6, 4, None, None, 1, 6, 4, 0, None, 0, 6, 3, 0, None, 5, 5, None, None, None, None, 2,
         None, 3, 6, None, 3, 0, 5, 0, 1, 0, 3, 4, 9, 9, 2, 7, 3, 8, 6, 9, None, 5, 8, None, None, None, None, 9, 8, 0, 7, None, None, 8, 8, 6, 6, 0, 2, 7, 4, 2, 3, 8, 6, 4, None, 8, None, None, None,
         2, 0, None, 1, 3, 5, 4, 2, 2, 5, 8, 8, None, 3, 0, None, 1, 6, 0, None, None, 9, None, 2, None, 6, 8, 2, None, None, 5, None, None, None, 9, 6, 6, 4, 2, 0, None, None, 1, None, 0, None, None,
         None, 6, 6, None, None, None, 4, 7, 9, None, 0, 1, None, None, 9, None, None, None, 4, None, 8, None, None, None, None, None, None, 4, None, 6, None, 3, None, None, 5, 1, 2, 5, None, 0, 7, 8,
         None, 7, None, None, 4, None, 4, 4, None, 2, None, 6, None, None, None, 7, None, None, None, None, 6, 4, None, 6, None, 6, 9, None, None, None, 9, 6, None, 9, None, 3, None, 2, None, 7, 7,
         None, None, 0, None, 6, 3, None, None, None, None, None, None, 1, None, None, None, 6, 9, 7, None, 7, None, 9, 3, 3, None, None, None, None, 4, None, None, 3, None, None, None, 3, 9, None, 0,
         3, 1, 9, 6, 7, 9, 4, 8, None, None, 6, None, 1, 3, 7, None, None, None, 3, None, 2, None, 8, 1, 1, None, None, 6, None, 7, 3, 5, None, 6, 3, 4, None, None, 5, 7, 1, None, None, 6, 4, 6, None,
         None, None, None, 5, 7, 0, 7, 0, None, 5, 8, 5, 5, 4, 5, None, None, None, None, None, None, 1, 7, None, None, 7, None, 9, 9, 6, 4, None, None, 3, 2, 1, None, 0, None, 0, 6, None, None, None,
         1, 5, None, None, None, 8, None, None, None, None, 3, 4, 8, None, None, 9, 6, 4, None, None, None, None, 8, 9, None, 1, None, None, None, 7, None, None, None, None, None, 9, None, None, None,
         4, 1, 6, 7, 0, None, None, None, 7, None, None, 8, None, None, None, None, None, None, None, 4, None, 9, None, None, None, None, 3, 0, 6, None, 5, None, 9, 9, None, None, 4, 3, 4, None, None,
         None, None, 8, None, 5, None, None, None, None, 5, 2, None, None, None, None, None, None, None, 2, None, None, 2, 1, 8, 5, None, 0, None, 0, 3, 2, 4, 5, None, None, None, None, None, 7, None,
         None, 0, None, 0, None, None, None, 0, 3, 9, None, None, None, None, 5, None, None, 0, 5, 0, 0, None, 9, None, None, None, None, None, None, None, None, 8, None, 9, 3, 5, 9, 0, 5, 9, None,
         None, 9, 4, None, 0, 2, 0, None, None, 7, None, 7, None, 5, 7, 8, 7, None, None, None, 3, 0, 3, None, None, None, None, None, 4, 5, None, None, 2, 3, None, 2, None, None, 7, None, None, 9,
         None, None, 9, 7, 1, None, None, 1, 6, 1, 8, None, None, 5, None, None, 3, 7, 9, 6, None, None, None, None, 1, None, None, None, 3, 7, 3, 2, 3, 3, None, 1, None, None, None, 1, None, None, 4,
         3, 4, 8, 7, None, 0, 3, 0, None, 1, 1, None, None, None, None, None, 5, None, 6, 0, None, 3, 1, None, 6, None, None, 4, 0, 1, None, 6, 1, None, None, 9, 6, 4, 9, 0, 8, 9, 3, 3, 6, None, None,
         None, None, None, None, None, None, None, None, None, None, 2, None, None, None, None, None, 8, 5, 8, 3, 5, 4, None, 6, None, 0, None, None, 6, None, 4, 3, None, None, None, None, None, None,
         None, None, None, None, None, None, None, None, 7, 3, None, None, 1, None, 2, 4, None, None, None, 6, None, None, None, 6, None, 5, None, None, None, None, 1, None, None, 3, None, 1, None, 7,
         1, None, None, 7, 1, 3, 4, 8, None, None, None, None, None, 4, None, None, 4, None, None, None, 7, None, 6, None, None, 1, None, None, None, 7, 3, 3, None, None, None, None, 3, 0, None, None,
         4, None, None, None, None, None, None, None, None, None, None, 8, None, None, 9, None, None, 6, 6, 5, 2, None, 8, 3, 8, None, None, None, None, 6, 7, 0, None, None, None, None, 1, 1, 5, None,
         0, 5, None, 5, None, None, None, 1, 2, None, 2, 9, 1, None, 2, 4, 1, None, None, None, 1, 8, 4, 4, 5, 2, None, None, 6, 4, 7, 5, 2, 9, None, 4, None, None, None, None, None, 3, None, None, 5,
         9, None, None, None, None, 9, None, 9, None, None, None, 2, None, 1, 9, None, None, None, None, None, 1, 9, 3, None, None, 1, 9, None, 5, 2, 1, 0, None, None, 1, 9, 8, 4, 7, None, None, 5, 7,
         None, None, None, None, 1, 2, 8, None, 6, 0, None, None, None, None, 0, None, None, None, 6, None, 2, 3, 0, 9, None, None, 1, 4, 6, None, 8, None, None, 5, None, 3, 0, None, 6, None, None,
         None, None, None, 2, None, None, None, None, None, None, 2, 5, 8, 6, 9, None, None, None, 8, None, None, 9, 6, None, None, None, None, 3, None, None, None, None, 9, None, None, 2, None, None,
         None, None, None, None, 8, 8, None, None, None, None, None, 9, None, 6, None, 2, 5, None, None, 1, 2, None, 4, None, None, 4, None, None, 3, 5, None, 3, 3, None, None, 1, None, None, None,
         None, 4, None, 2, 3, None, 4, 5, 3, None, 7, None, None, None, 7, 6, None, None, 1, 3, None, 4, 9, 8, None, None, 0, None, 3, 4, None, 8, None, 1, None, None, 2, 2, None, None, 4, None, None,
         None, 3, None, None, 2, None, None, None, 4, None, 5, None, None, None, None, 2, None, 5, None, None, None, None, None, None, 2, 7, 5, None, 6, None, None, None, None, 2, None, 0, None, 3,
         None, 1, None, 9, 4, None, 3, None, None, None, None, None, None, None, 5, 5, 7, None, None, 1, None, 4, 6, None, None, None, 2, None, 5, 9, 0, 6, 2, None, None, None, None, None, None, None,
         None, None, None, None, None, 5, None, 7, None, 2, 9, None, None, 1, None, None, None, 1, 6, None, 6, None, None, 0, 8, None, 4, None, None, None, None, 4, None, None, 0, None, 6, 0, None,
         None, None, 4, None, None, None, None, None, 0, None, None, None, None, None, None, None, None, None, None, None, None, 0, 5, 4, 2, 6, 4, 5, 3, 4, None, None, 5, None, None, None, None, 4,
         None, None, 3, 6, 2, 0, None, 6, 6, None, None, None, None, 0, 6, None, None, None, 3, 9, 4, None, None, None, None, None, 0, None, None, 6, 7, 0, None, 9, 2, None, 3, 3, None, None, 8, None,
         3, None, None, None, 8, 5, 3, None, 2, 4, None, 9, 6, 9, None, None, None, None, 6, None, 6, None, 5, 3, None, None, None, None, 4, None, None, None, 9, 0, 9, 7, 1, 1, None, 1, None, 1, 6,
         None, 5, None, 6, None, None, 1, None, None, None, None, None, None, 5, None, None, None, None, None, 3, None, 6, 1, None, 0, 2, None, None, 0, None, None, 0, None, None, None, None, None, 3,
         None, None, 8, None, None, 5, 3, 3, None, None, None, None, None, None, None, 3, None, None, 0, 8, 7, None, None, 8, 1, None, None, None, None, None, None, 7, None, None, None, None, None,
         None, None, None, None, None, None, 5, 2, None, 2, 6, None, None, None, None, None, None, None, 1, 5, 0, None, None, 2, None, 7, None, None, 6, None, None, None, None, None, None, None, None,
         None, None, None, None, None, 8, None, None, None, None, 3, None, None, 4, None, None, 2, None, None, None, None, 0, 3, None, None, None, None, None, 7, None, 8, None, None, None, None, 8, 5,
         None, 3, 4, None, None, None, 8, None, None, None, None, None, None, None, None, None, 3, 7, None, None, None, 4, 0, 3, None, None, 6, None, None, None, None, None, None, None, None, None,
         None, None, None, 8, None, None, None, None, None, 2, None, None, None, None, None, None, None, None, None, 0, None, None, None, 2, None, None, None, 8, 2, None, None, None, None, None, None,
         None, 8, None, None, None, None, None, None, None, None, None, None, 2, None, None, None, 2, 5, None, None, None, None, None, None, None, None, None, None, None, 2, None, None, None, None,
         None, 8, None, None, None, None, None, None, None, None, None, None, 0, 5])))
