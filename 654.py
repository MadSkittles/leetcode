from common import TreeNode


class Solution:
    def constructMaximumBinaryTree(self, nums):
        if not nums:
            return None
        max_num = max(nums)
        max_pos = nums.index(max_num)
        node = TreeNode(max_num)
        node.left, node.right = self.constructMaximumBinaryTree(nums[:max_pos]), self.constructMaximumBinaryTree(nums[max_pos + 1:])
        return node


if __name__ == '__main__':
    solution = Solution()
    print(solution.constructMaximumBinaryTree([3, 2, 1, 6, 0, 5]))
