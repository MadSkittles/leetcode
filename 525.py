# 类似于523，若sum(0...i)=[x1, y1](x1是0的个数，y1是1的个数)，若有j>i，sum(0...j)=[x2, y2]，且y2-x2=y1-x2，
# 则可知sum(i+1...j)=[x, y]，其中x=y

class Solution:
    def findMaxLength(self, nums):
        res, ac, seen = 0, [0, 0], {0: -1}
        for index, n in enumerate(nums):
            ac[n] += 1
            if (ac[1] - ac[0]) not in seen:
                seen[ac[1] - ac[0]] = index
            else:
                res = max(res, index - seen[ac[1] - ac[0]])
        return res
