class Solution:
    def bulbSwitch(self, n):
        sum, base, time = 0, 0, 3
        while sum < n:
            sum += time
            base += 1
            time += 2
        return base


if __name__ == '__main__':
    solution = Solution()
    res = []
    for i in range(3, 100):
        r = solution.bulbSwitch(i)
        print(i, r)
        res.append(r)
    from collections import Counter

    print(Counter(res))
