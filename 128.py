class Solution:
    def longestConsecutive(self, nums):
        res, range_map = 0, {}
        for n in nums:
            if n not in range_map:
                l = r = n
                if l - 1 in range_map:
                    l, _ = range_map[l - 1]
                if r + 1 in range_map:
                    _, r = range_map[r + 1]
                range_map[n] = [l, r]
                range_map[l] = [l, r]
                range_map[r] = [l, r]
                res = max(res, r - l + 1)
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestConsecutive([0, 0]))
