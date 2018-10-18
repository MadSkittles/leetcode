class Solution:
    def fairCandySwap(self, A, B):
        sum_a, sum_b = sum(A), sum(B)
        base = -1 if sum_a > sum_b else 1
        diff = abs(sum_a - sum_b) // 2
        B = set(B)
        for n in A:
            if (n + base * diff) in B:
                return [n, n + base * diff]
