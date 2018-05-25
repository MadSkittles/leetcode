class Solution:
    def majorityElement(self, nums):
        n, cnt = None, 0
        for i in nums:
            if cnt == 0:
                n = i
            if i == n:
                cnt += 1
            else:
                cnt -= 1
        return n


if __name__ == '__main__':
    solution = Solution()
    print(solution.majorityElement([2,2,1,1,1,2,2]))
