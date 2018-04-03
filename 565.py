class Solution:
    def arrayNesting(self, nums):
        visited, res = set(), 0
        for index, n in enumerate(nums):
            if index not in visited:
                d, i = {}, 0
                while n not in d:
                    d[n] = i
                    i += 1
                    n = nums[n]
                res = max(res, len(d) - d[n])
                visited.update(d.keys())
        return res