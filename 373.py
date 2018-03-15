class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        import heapq
        return heapq.nsmallest(k, ([u, v] for u in nums1 for v in nums2), key=sum)


if __name__ == '__main__':
    solution = Solution()
    print(solution.kSmallestPairs(
        [34, 774, 1640, 1814, 2364, 2733, 2872, 3556, 4310, 4344, 4850, 5158, 6062, 6778, 7542, 8115, 8590, 9071, 9204,
         10021, 10288, 10987, 11850, 12773, 12948, 13940, 14475, 14572, 15254, 15730, 16287, 17010, 17698, 18014, 18128,
         18692, 18804, 19283, 19804, 20386, 20763, 20808, 21600, 22144, 22982, 23535, 23861, 23982, 24938, 25251, 25663,
         26298, 26939, 27077, 27419, 27997, 28809, 28975, 29904, 30717, 30886, 31853, 32433, 33338, 33878, 33881, 34266,
         34685, 35239, 35455, 36153, 36493, 36650, 37184, 37310, 38178, 38304, 39298, 40029, 40430, 41145, 41288, 41395,
         41633, 42625, 43613, 43798, 44733, 45332, 45470, 45944, 46657, 47307, 48232, 48463, 49443, 49736, 50240, 51119,
         52041],
        [801, 933, 1093, 1498, 2384, 2665, 3310, 4119, 4786, 4975, 5292, 6132, 6344, 6818, 7448, 8264, 8904, 9118,
         10053, 10745, 11671, 12517, 12558, 12819, 12843, 13750, 13765, 14481, 14787, 14922, 15824, 15892, 16879, 17151,
         18100, 18208, 18866, 19414, 20372, 20551, 20856, 21547, 21917, 22879, 23389, 24317, 24974, 25051, 25367, 26047,
         26942, 27711, 28453, 28629, 28972, 29587, 30559, 31377, 32077, 33036, 33784, 34480, 35178, 35640, 36386, 37225,
         37482, 38338, 38481, 39286, 39680, 40533, 41354, 41965, 42268, 42619, 43027, 43631, 44109, 44191, 44245, 45240,
         45303, 46106, 46810, 47282, 47859, 48212, 48378, 48549, 49229, 49548, 50354, 50521, 51411, 52322, 52792, 53256,
         53388, 53571],
        1000))