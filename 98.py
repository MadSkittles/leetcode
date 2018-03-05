from common import TreeNode


class Solution:
    def isValidBST(self, root):
        return self.f(root)[0]

    def f(self, node, d=0):
        if node is None:
            return True, None
        left_result, left_max = self.f(node.left, -1)
        right_result, right_min = self.f(node.right, 1)

        res, p = node.val, node
        while d < 0 and p.right:
            p = p.right
        while d > 0 and p.left:
            p = p.left

        return left_result and right_result and (not left_max or left_max < node.val) \
               and (not right_min or right_min > node.val), p.val


if __name__ == '__main__':
    solution = Solution()
    print(solution.isValidBST(TreeNode.list2Tree([3,None,30,10,None,None,15,None,45])))
