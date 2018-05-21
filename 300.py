class Solution:
    def lengthOfLIS(self, nums):
        length = []
        for i in range(len(nums)):
            length.append(max([length[j] + 1 for j in range(i - 1, -1, -1) if nums[i] > nums[j]] + [1]))
        return max(length + [0])

    def lengthOfLIS1(self, nums):
        import bisect
        tails = []
        for n in nums:
            idx = bisect.bisect_left(tails, n)
            if idx == len(tails):
                tails.append(n)
            else:
                tails[idx] = n
        return len(tails)


if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLIS1([10, 9, 2, 5, 3, 7, 101, 18]))
