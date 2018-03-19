# 假设灯泡K会被开关x次，那么只有当x为奇数时，这个灯泡才会最终是点亮状态。x的次数等于K的因子数目，K的因子都是成对出现的，如K=12时，因子包括
# 1-12、2-6、3-4，所以K的因子数都是偶数，除非当K为平方数时，这时有一对因子是相同的，这时因子数为奇数，所以最终亮着的灯泡个数为小于等于K的
# 平方数的个数。

class Solution:
    def bulbSwitch(self, n):
        return int(n ** 0.5)


if __name__ == '__main__':
    solution = Solution()
    for i in range(1, 100):
        print(i, solution.bulbSwitch(i))