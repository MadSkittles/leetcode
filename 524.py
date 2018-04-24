class Solution:
    def findLongestWord(self, s, d):
        self.m = {}
        for index, c in enumerate(s):
            self.m.setdefault(c, []).append(index)
        res = ''
        for dd in d:
            if self.isSubsequence(dd) and (len(dd) > len(res) or (len(dd) == len(res) and dd < res)):
                res = dd
        return res

    def isSubsequence(self, s):
        import bisect
        index = -1
        for c in s:
            if index > self.m.get(c, [float('-inf')])[-1]:
                return False
            index = self.m[c][bisect.bisect_left(self.m[c], index)] + 1
        return True