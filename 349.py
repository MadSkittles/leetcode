class Solution:
    def intersection(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        res, p1, p2 = [], 0, 0
        while p1 < len(nums1) or p2 < len(nums2):
            n1 = nums1[p1] if p1 < len(nums1) else float('inf')
            n2 = nums2[p2] if p2 < len(nums2) else float('inf')
            if n1 == n2:
                res.append(n1)
            if n1 <= n2:
                while p1 < len(nums1) and nums1[p1] == n1:
                    p1 += 1
            if n1 >= n2:
                while p2 < len(nums2) and nums2[p2] == n2:
                    p2 += 1
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.intersection([], [2, 2]))
