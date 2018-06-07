from common import TreeNode


class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        floor, res = [root], 0
        while floor:
            res += 1
            next = []
            for node in floor:
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)
            floor = next
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxDepth(TreeNode.list2Tree([3, 9, 20, None, None, 15, 7])))
