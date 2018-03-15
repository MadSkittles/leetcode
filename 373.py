class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        return sorted([(i,j) for i in nums1 for j in nums2],key=lambda x:sum(x))[:k]


if __name__ == '__main__':
    solution = Solution()
    print(solution.kSmallestPairs([1, 7, 11, 12], [2, 3, 4], 9))
