class Solution:
    def maxSlidingWindow(self, nums, k):
        if not nums:
            return []
        max_ = max(nums[:k])
        res = [max_]
        for i in range(k, len(nums)):
            if nums[i] > max_:
                max_ = nums[i]
            elif nums[i - k] != max_:
                max_ = max(max_, nums[i])
            else:
                max_ = max(nums[i - k + 1:i + 1])
            res.append(max_)
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxSlidingWindow([], 0))
