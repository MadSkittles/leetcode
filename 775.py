class Solution:
    def isIdealPermutation(self, A):
        return not any(abs(i - v) > 1 for i, v in enumerate(A))
