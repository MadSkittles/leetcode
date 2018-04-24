class Solution:
    def frequencySort(self, s):
        from collections import Counter
        c = Counter(s)
        return ''.join(sorted(s, key=lambda x: (c[x], x), reverse=True))

    def frequencySort1(self, s):
        from collections import Counter
        res, c, bucket = '', Counter(s), [[] for _ in range(len(s) + 1)]
        for k in c:
            bucket[c[k]].append(k)
        for i in range(len(s), 0, -1):
            for ch in bucket[i]:
                res += ch * i
        return res


if __name__ == '__main__':
    solutioin = Solution()
    print(solutioin.frequencySort1("loveleetcode"))
