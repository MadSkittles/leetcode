class Solution:
    def findSubsequences(self, nums):
        res = set()
        for n in nums:
            new_seq = set()
            for r in res:
                if n >= r[-1]:
                    new_seq.add((*r, n))
            res.update(new_seq)
            res.add((n,))
        return [n for n in res if len(n) > 1]