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
        cur = -1
        for c in s:
            if c not in self.m:
                return False
            else:
                index = self.m[c]
                for i in index:
                    if i > cur:
                        cur = i
                        break
                else:
                    return False
        return True