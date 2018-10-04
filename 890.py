class Solution:
    def findAndReplacePattern(self, words, pattern):
        res = []
        for word in words:
            if len(word) != len(pattern):
                continue
            w2p, p2w, flag = {}, {}, True
            for w, p in zip(word, pattern):
                if w not in w2p and p not in p2w:
                    w2p[w], p2w[p] = p, w
                elif (w in w2p and w2p[w] != p) or (p in p2w and p2w[p] != w):
                    flag = False
                    break
            if flag:
                res.append(word)
        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.findAndReplacePattern(["abc", "deq", "mee", "aqq", "dkd", "ccc"], "abb"))

