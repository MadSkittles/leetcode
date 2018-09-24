from common import TreeNode


class Solution:
    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1 :])
        return root


if __name__ == "__main__":
    solution = Solution()
    print(solution.sortedArrayToBST([-10, -3, 0, 5, 9]))
