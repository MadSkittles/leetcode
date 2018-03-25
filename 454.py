class Solution:
    def fourSumCount(self, A, B, C, D):
        from collections import Counter
        c = Counter(i + j for i in A for j in B)
        return sum(c.get(-i - j, 0) for i in C for j in D)