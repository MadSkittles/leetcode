class Solution:
    def expressiveWords(self, S, words):
        res, S = 0, self.seprate(S)
        for word in words:
            w = self.seprate(word)
            if not len(S) == len(w):
                continue
            for i in range(len(S)):
                if (len(S[i]) < 3 and w[i] != S[i]) or (len(S[i]) >= 3 and S[i][:len(w[i])] != w[i]):
                    break
            else:
                res += 1
        return res

    def seprate(self, s):
        res, ss = [], ''
        for i, c in enumerate(s):
            if i > 0 and c != s[i - 1]:
                res.append(ss)
                ss = ''
            ss += c
        res.append(ss)
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.expressiveWords("heeellooo", ["hello", "hi", "helo"]))
