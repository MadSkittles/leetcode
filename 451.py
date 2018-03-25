class Solution:
    def frequencySort(self, s):
        from collections import Counter
        c = Counter(s)
        return ''.join(sorted(s, key=lambda x: (c[x], x), reverse=True))
