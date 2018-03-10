class Solution:
    def getHint(self, secret, guess):
        bull = 0
        diff_s, diff_g = [], []
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bull += 1
            else:
                diff_s.append(secret[i])
                diff_g.append(guess[i])
        cow = 0
        from collections import Counter
        diff_s, diff_g = Counter(diff_s), Counter(diff_g)
        for i in diff_g:
            if i in diff_s:
                cow += min(diff_s[i], diff_g[i])
        return str(bull) + 'A' + str(cow) + 'B'


if __name__ == '__main__':
    solution = Solution()
    print(solution.getHint('1807', '7810'))
