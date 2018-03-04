from common import TreeNode


class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        res = []
        p = [root]
        while p:
            vals = []
            next_floor_node = []
            for node in p:
                vals.append(node.val)
                if node.left:
                    next_floor_node.append(node.left)
                if node.right:
                    next_floor_node.append(node.right)
            res.append(vals)
            p = next_floor_node
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.levelOrder(TreeNode.list2Tree([3, 9, 20, None, None, 15, 7])))
