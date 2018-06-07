class Solution:
    def smallestDistancePair(self, nums, k):
        import bisect
        nums.sort()
        l, r = min(nums[i + 1] - nums[i] for i in range(len(nums) - 1)), nums[-1] - nums[0]
        while l < r:
            m = (l + r) // 2
            c = sum(bisect.bisect_right(nums, nums[i] + m, i + 1) - i - 1 for i in range(len(nums) - 1))
            if c >= k:
                r = m
            else:
                l = m + 1
        return l


if __name__ == '__main__':
    solution = Solution()
    print(solution.smallestDistancePair([9, 10, 7, 10, 6, 1, 5, 4, 9, 8],
                                        18))
