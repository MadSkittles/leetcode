# boyer-moore vote algorithm

class Solution:
    def majorityElement(self, nums):
        candidate1, count1, candidate2, count2 = None, 0, None, 0
        for n in nums:
            if count1 <= 0 and n != candidate2:
                candidate1 = n
                count1 = 0
            if count2 <= 0 and n != candidate1:
                candidate2 = n
                count2 = 0

            if n == candidate1:
                count1 += 1
            elif n == candidate2:
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        return [n for n in (candidate1, candidate2)
                if nums.count(n) > len(nums) // 3]

    def majorityElementGeneral(self, nums, n):
        candidates = [[None, 0] for _ in range(n - 1)]
        for n in nums:
            for candidate in candidates:
                if candidate[1] <= 0 and n not in [c for c, _ in candidates]:
                    candidate[0] = n
                    candidate[1] = 0
            flag = True
            for candidate in candidates:
                if n == candidate[0]:
                    candidate[1] += 1
                    flag = False
            if flag:
                for candidate in candidates:
                    candidate[1] -= 1
        return [candidate[0] for candidate in candidates if nums.count(candidate[0]) > len(nums) // n]


if __name__ == '__main__':
    solution = Solution()
    l = [1, 1, 1, 1, 1, 4, 5, 6]
    print(solution.majorityElementGeneral(l, 2))
