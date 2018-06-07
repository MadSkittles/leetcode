from common import TreeNode


class Solution:
    def minDepth(self, root):
        if not root:
            return 0
        f, floor = [root], 0
        while f:
            floor += 1
            next = []
            for node in f:
                if not node.left and not node.right:
                    return floor
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)
            f = next


if __name__ == '__main__':
    solution = Solution()
    print(solution.minDepth(TreeNode.list2Tree([3, 9, 20, None, None, 15, 7])))
