class Solution:
    def canCompleteCircuit(self, gas, cost):
        max_reach, i = 0, 0
        while i < len(gas):
            pos, left, length = i, gas[i], 0
            while left >= cost[pos % len(gas)] and length < len(gas):
                left -= cost[pos % len(gas)]
                pos += 1
                left += gas[pos % len(gas)]
                length += 1
            if length == len(gas):
                return i
            else:
                i = pos + 1
        return -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.canCompleteCircuit([2, 4], [3, 4]))
