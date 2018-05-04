class Solution:
    def merge(self, nums1, m, nums2, n):
        import bisect
        lo = 0
        for n in nums2:
            pos = bisect.bisect_right(nums1, n, lo, m)
            if pos < m:
                for i in range(m - 1, pos - 1, -1):
                    nums1[i + 1] = nums1[i]
            nums1[pos] = n
            m += 1
            lo = pos + 1


if __name__ == '__main__':
    solution = Solution()
    nums1 = [1, 0, 0, 0]
    nums2 = [2, 2, 2]
    solution.merge(nums1, 1, nums2, 3)
    print(nums1)
