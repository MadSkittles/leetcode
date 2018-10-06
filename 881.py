class Solution:
    def numRescueBoats(self, people, limit):
        people.sort()
        res, lo, hi = 0, 0, len(people) - 1
        while lo < hi:
            if people[lo] + people[hi] <= limit:
                lo += 1
                hi -= 1
            else:
                hi -= 1
            res += 1
        res += lo == hi
        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.numRescueBoats([1, 2], 3))
    print(solution.numRescueBoats([3, 2, 2, 1], 3))
    print(solution.numRescueBoats([3, 5, 3, 4], 5))
