class Solution:
    def hIndex(self, citations):
        res, total, cnt = 0, len(citations), 1
        for i in range(1, len(citations) + 1):
            if i >= len(citations) or citations[i] != citations[i - 1]:
                res = max(res, min(citations[i - 1], total))
                total -= cnt
                cnt = 1
            else:
                cnt += 1
        return res