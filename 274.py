class Solution:
    def hIndex(self, citations):
        from collections import Counter
        c = sorted(Counter(citations).items(),key=lambda x:x[0])
        total = len(citations)
        res = 0
        for i,c_num in c:
            res = max(res, min(total, i))
            total -= c_num
        return res